# from django.http import HttpResponse
from django.shortcuts import render
from .forms import BookingForm
from .models import Menu
from django.core import serializers
from .models import Booking
from datetime import datetime, date
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from django.utils.dateparse import parse_date


# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def reservations(request):
    bookings = Booking.objects.all()
    booking_json = serializers.serialize('json', bookings)
    return render(request, 'bookings.html',{"bookings":booking_json})

def all_reservations(request):
    #Collect Expired Bookings and delete them
    Booking.objects.filter(reservation_date__lt=date.today()).delete()

    #Collect all current bookings available
    bookings = Booking.objects.exclude(first_name__isnull=True).exclude(reservation_date__isnull=True).exclude(reservation_slot__isnull=True)

    return render(request, 'bookings.html', {'bookings': bookings})

def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'book.html', context)

def menu(request):
    menu_data = Menu.objects.all()
    main_data = {"menu": menu_data}
    return render(request, 'menu.html', {"menu": main_data})


def display_menu_item(request, pk=None): 
    if pk: 
        menu_item = Menu.objects.get(pk=pk) 
    else: 
        menu_item = "" 
    return render(request, 'menu_item.html', {"menu_item": menu_item}) 

@csrf_exempt
def bookings(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)  # Read JSON body safely

            # Check if a booking already exists for the same date and slot
            exists = Booking.objects.filter(
                reservation_date=data.get('reservation_date'),
                reservation_slot=data.get('reservation_slot')
            ).exists()

            if not exists:
                Booking.objects.create(
                    first_name=data.get('first_name'),
                    reservation_date=data.get('reservation_date'),
                    reservation_slot=data.get('reservation_slot'),
                )
                return JsonResponse({'success': True, 'message': 'Booking created successfully'})
            else:
                return JsonResponse({'success': False, 'error': 'Slot already booked'}, status=400)
            
        except json.JSONDecodeError:
            return JsonResponse({'success': False, 'error': 'Invalid JSON format'}, status=400)
        except KeyError as e:
            return JsonResponse({'success': False, 'error': f'Missing key: {str(e)}'}, status=400)
        
    # Handling GET request to fetch bookings
    date_param = request.GET.get('date', datetime.today().date())

    # Simplified the booking data structure for better clarity
    bookings = Booking.objects.filter(reservation_date=date_param)
    booking_data = [
        {
            'first_name': booking.first_name,
            'reservation_slot': booking.reservation_slot
        }
        for booking in bookings
    ]

    reserved_slots = [booking.reservation_slot for booking in bookings]  # Collect reserved slots

    # Available slots as numbers (no formatting here)
    available_slots = [10, 12, 14, 16, 18, 20]  # 24-hour format, integer values

    # Return bookings and available slots as integers
    return JsonResponse({
        'bookings': booking_data,
        'available_slots': available_slots,
        'reserved_slots': reserved_slots
    })


    #     data = json.load(request)
    #     exist = Booking.objects.filter(reservation_date=data['reservation_date']).filter(
    #         reservation_slot=data['reservation_slot']).exists()
    #     if exist==False:
    #         booking = Booking(
    #             first_name=data['first_name'],
    #             reservation_date=data['reservation_date'],
    #             reservation_slot=data['reservation_slot'],
    #         )
    #         booking.save()
    #     else:
    #         return HttpResponse("{'error':1}", content_type='application/json')
    
    # date = request.GET.get('date',datetime.today().date())

    # bookings = Booking.objects.all().filter(reservation_date=date)
    # booking_json = serializers.serialize('json', bookings)

    # return HttpResponse(booking_json, content_type='application/json')