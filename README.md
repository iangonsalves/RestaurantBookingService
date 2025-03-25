# Little Lemon Restaurant Booking System

Little Lemon is a restaurant booking system built with Django that allows users to place bookings, view reservations, and manage their restaurant appointments.

## Project Structure
```
finalbookingexercise/
├── littlelemon/            # Project folder
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── restaurant/             # App folder
│   ├── migrations/         # Django migrations
│   ├── static/             # Static files (CSS, JS, Images)
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
└── virtualenv/             # Virtual environment
```

## Features
- **Home Page:** Welcomes users to Little Lemon.
- **About Page:** Provides details about the restaurant.
- **About Page:** Provides details about the current menu.
- **Booking Page:** Allows users to place a booking and view existing bookings for a selected date.
- **Reservations Page:** Displays all reservations placed at the restaurant.

## Setup Instructions
1. **Clone the repository:**
```bash
git clone <repository-url>
cd restaurantbookingservice
```

2. **Activate the virtual environment:**
```bash
source ../virtualenv/bin/activate  # MacOS/Linux
..\virtualenv\Scripts\activate    # Windows
```

3. **Install dependencies:**
```bash
pipenv install
```

4. **Run migrations:**
```bash
python manage.py makemigrations
python manage.py migrate
```

5. **Run the server:**
```bash
python manage.py runserver
```
Access the project at `https://restaurantbookingservice.onrender.com`

## Endpoints
- Home Page: `/`
- About Page: `/about/`
- Menu Page: `/menu`
- Booking Page: `/book/`
- Reservations Page: `/reservations/`

## Database
The project uses MySQL for handling reservations. Ensure the database is properly configured in `settings.py`.

---
Enjoy managing your reservations with Little Lemon! 🍋
