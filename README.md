
# Travel_App

# Django Destination API

This is a Django RESTful API for managing destinations.

## Setup

1. Clone the repository:
'''bash
   git clone https://github.com/yourusername/django-destination-api.git



Certainly! Below is a basic README.md file template for your Django project:

markdown
Copy code
# Django Destination API

This is a Django RESTful API for managing destinations.

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/Adi7936/django-destination-api.git
   
2.Install dependencies:
pip install -r requirements.txt


3.Apply migrations:
python3 manage.py migrate
a. create super user:
python3 manage.py createsuperuser

4.Run Server:
python3 manage.py runserver

Running Tests::
python manage.py test


API Endpoints::

Destination List/Create
Endpoint: /api/destinations/
Method: GET (List all destinations) / POST (Create a new destination)
ex: [
    {
        "id": 1,
        "name": "heggar",
        "country": "India",
        "description": "dkkbd",
        "best_time_to_visit": "10",
        "category": "Beach",
        "image_url": "https://image.com",
        "created_at": "2024-04-02T07:29:37.939872Z",
        "updated_at": "2024-04-02T07:29:37.939909Z"
    }
]


Destination Retrieve/Update/Destroy
Endpoint: /api/destinations/<destination_id>/
Method: GET (Retrieve a destination) / PUT (Update a destination) / DELETE (Delete a destination)
ex: http://127.0.0.1:8000/api/destinations/1
 [
    {
        "id": 1,
        "name": "heggar",
        "country": "India",
        "description": "dkkbd",
        "best_time_to_visit": "10",
        "category": "Beach",
        "image_url": "https://image.com",
        "created_at": "2024-04-02T07:29:37.939872Z",
        "updated_at": "2024-04-02T07:29:37.939909Z"
    }
]
