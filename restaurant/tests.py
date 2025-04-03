from django.test import TestCase, Client
from django.urls import reverse
from .models import Booking, Menu
from .forms import BookingForm
from datetime import date
import json

class BookingModelTest(TestCase):
    def setUp(self):
        """Set up test data for Booking model tests."""
        self.booking_data = {
            'first_name': 'John Doe',
            'reservation_date': date.today(),
            'reservation_slot': 10
        }
        self.booking = Booking.objects.create(**self.booking_data)

    def test_booking_creation(self):
        """Test if a booking can be created with valid data."""
        self.assertEqual(self.booking.first_name, 'John Doe')
        self.assertEqual(self.booking.reservation_date, date.today())
        self.assertEqual(self.booking.reservation_slot, 10)

    def test_booking_str(self):
        """Test the string representation of a booking."""
        expected_str = f"{self.booking.first_name} - {self.booking.reservation_date} - {self.booking.reservation_slot}"
        self.assertEqual(str(self.booking), expected_str)

    def test_duplicate_booking(self):
        """Test that duplicate bookings for same date and slot are prevented."""
        with self.assertRaises(Exception):
            Booking.objects.create(**self.booking_data)

class MenuModelTest(TestCase):
    def setUp(self):
        """Set up test data for Menu model tests."""
        self.menu_data = {
            'name': 'Test Dish',
            'price': 15,
            'menu_item_description': 'A delicious test dish',
            'image_filename': 'test.jpg'
        }
        self.menu_item = Menu.objects.create(**self.menu_data)

    def test_menu_creation(self):
        """Test if a menu item can be created with valid data."""
        self.assertEqual(self.menu_item.name, 'Test Dish')
        self.assertEqual(self.menu_item.price, 15)
        self.assertEqual(self.menu_item.menu_item_description, 'A delicious test dish')
        self.assertEqual(self.menu_item.image_filename, 'test.jpg')

    def test_menu_str(self):
        """Test the string representation of a menu item."""
        self.assertEqual(str(self.menu_item), 'Test Dish')

class BookingFormTest(TestCase):
    def test_valid_form(self):
        """Test if the form is valid with correct data."""
        form_data = {
            'first_name': 'John Doe',
            'reservation_date': date.today(),
            'reservation_slot': 10
        }
        form = BookingForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        """Test if the form is invalid with incorrect data."""
        form_data = {
            'first_name': '',  # Empty name
            'reservation_date': date.today(),
            'reservation_slot': 10
        }
        form = BookingForm(data=form_data)
        self.assertFalse(form.is_valid())

class ViewTest(TestCase):
    def setUp(self):
        """Set up test client and create test data."""
        self.client = Client()
        self.booking = Booking.objects.create(
            first_name='John Doe',
            reservation_date=date.today(),
            reservation_slot=10
        )
        self.menu_item = Menu.objects.create(
            name='Test Dish',
            price=15,
            menu_item_description='Test Description'
        )

    def test_home_view(self):
        """Test if home view renders correctly."""
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_about_view(self):
        """Test if about view renders correctly."""
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')

    def test_menu_view(self):
        """Test if menu view renders correctly with menu items."""
        response = self.client.get(reverse('menu'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'menu.html')
        self.assertIn('menu', response.context)

    def test_display_menu_item_view(self):
        """Test if menu item detail view renders correctly."""
        response = self.client.get(reverse('menu_item', args=[self.menu_item.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'menu_item.html')
        self.assertEqual(response.context['menu_item'], self.menu_item)

class BookingAPITest(TestCase):
    def setUp(self):
        """Set up test client and create test data."""
        self.client = Client()
        self.booking = Booking.objects.create(
            first_name='John Doe',
            reservation_date=date.today(),
            reservation_slot=10
        )

    def test_get_bookings(self):
        """Test GET request to bookings API."""
        response = self.client.get(reverse('bookings'))
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertIn('bookings', data)
        self.assertIn('available_slots', data)
        self.assertIn('reserved_slots', data)

    def test_post_booking(self):
        """Test POST request to create a new booking."""
        booking_data = {
            'first_name': 'Jane Doe',
            'reservation_date': date.today().isoformat(),
            'reservation_slot': 12
        }
        response = self.client.post(
            reverse('bookings'),
            data=json.dumps(booking_data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertTrue(data['success'])

    def test_duplicate_booking_post(self):
        """Test POST request with duplicate booking data."""
        booking_data = {
            'first_name': 'John Doe',
            'reservation_date': date.today().isoformat(),
            'reservation_slot': 10  # Same slot as in setUp
        }
        response = self.client.post(
            reverse('bookings'),
            data=json.dumps(booking_data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.content)
        self.assertFalse(data['success'])
        self.assertEqual(data['error'], 'Slot already booked')
