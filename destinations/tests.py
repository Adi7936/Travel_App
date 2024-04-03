

from django.test import TestCase
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.urls import reverse
from .models import Destination


class DestinationModelTest(TestCase):

 def test_destination_creation(self):
    destination = Destination.objects.create(
        name='Test Destination',
        country='Test Country',
        description='Test Description',
        best_time_to_visit='Test Time',
        category='Beach',  # or any other valid category
        image_url='https://example.com/image.jpg'
    )
    
    self.assertEqual(destination.name, 'Test Destination')
    self.assertEqual(destination.country, 'Test Country')
    self.assertEqual(destination.description, 'Test Description')
    self.assertEqual(destination.best_time_to_visit, 'Test Time')
    self.assertEqual(destination.category, 'Beach')  # Ensure the category is set correctly
    self.assertEqual(destination.image_url, 'https://example.com/image.jpg')
    
    def test_destination_category_choices(self):
        destination = Destination.objects.create(
            name='Test Destination',
            country='Test Country',
            description='Test Description',
            best_time_to_visit='Test Time',
            category='Invalid Category',
            image_url='https://example.com/image.jpg'
        )
        with self.assertRaises(ValueError):
            destination.full_clean()


class DestinationAPITest(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_destination_list_create(self):
        url = reverse('destination-list-create')
        data = {
            "name": "Test Destination",
            "country": "Test Country",
            "description": "Test Description",
            "best_time_to_visit": "Test Time",
            "category": "Beach",
            "image_url": "https://example.com/image.jpg"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)  # Check if object created successfully

    def test_destination_retrieve_update_destroy(self):
        destination = Destination.objects.create(
            name='Test Destination',
            country='Test Country',
            description='Test Description',
            best_time_to_visit='Test Time',
            category='Beach',
            image_url='https://example.com/image.jpg'
        )
        url = reverse('destination-retrieve-update-destroy', kwargs={'pk': destination.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)  # Check if object retrieved successfully

        # Test update
        updated_data = {
            "name": "Updated Destination",
            "country": "Updated Country",
            "description": "Updated Description",
            "best_time_to_visit": "Updated Time",
            "category": "Mountain",
            "image_url": "https://example.com/updated_image.jpg"
        }
        response = self.client.put(url, updated_data, format='json')
        self.assertEqual(response.status_code, 200)  # Check if object updated successfully

        # Test delete
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)  # Check if object deleted successfully
