# Little Lemon Restaurant Booking System

Little Lemon is a restaurant booking system built with Django that allows users to place bookings, view reservations, and manage their restaurant appointments.

## Live Demo

Application URL:  
https://restaurantbookingservice.onrender.com/

<img width="1619" alt="restaurant" src="https://github.com/user-attachments/assets/1be47056-d40a-4349-9b97-d17673eeff50" />

## Tech Stack

Backend: Django (Python)  
Frontend: Django Templates, HTML, CSS  
Database: PostgreSQL  
Deployment: Render

## Project Structure
```
restaurantbookingservice/
│
├── littlelemon/            # Django project configuration
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── restaurant/             # Main application
│   ├── migrations/
│   ├── static/             # CSS, JavaScript, images
│   ├── templates/          # HTML templates
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── forms.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── requirements.txt        # Python dependencies
└── manage.py               # Django management script
```

## Key Features

- User authentication and account management
- Restaurant information and menu pages
- Online reservation system for selecting booking dates
- View existing bookings for selected dates
- Reservation listing for restaurant staff 
- Server-rendered web pages using Django templates  
- PostgreSQL database integration  
- Deployed on Render cloud platform


## Endpoints
- Home Page: `/`
- About Page: `/about/`
- Menu Page: `/menu`
- Booking Page: `/book/`
- Reservations Page: `/reservations/`


## Local Development Setup
1. **Clone the repository:**
```bash
git clone https://github.com/iangonsalves/RestaurantBookingService.git
```

2. **Create the virtual environment:**
```bash
python -m venv venv 
```

3. **Activate the environment:**
```bash
Mac/Linux:
source venv/bin/activate

Windows:
venv\Scripts\activate
```
4. **Install dependencies:**
```bash
pip install -r requirements.txt
```

5. **Run migrations:**
```bash
python manage.py makemigrations
python manage.py migrate
```

6. **Start the development server::**
```bash
python manage.py runserver
```

7. **Open in browser:**
```bash
http://127.0.0.1:8000
```


## Database
The project uses environment variables for database configuration. Create a `.env` file and configure the required database credentials for your local environment.


## Deployment
The application is deployed using Render.
The platform installs dependencies from `requirements.txt` and runs the Django application automatically

---
Enjoy managing your booking reservations with Little Lemon!