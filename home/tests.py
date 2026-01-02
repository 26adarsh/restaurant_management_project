from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from home.models import Restaurant
# Create your tests here.

class RestaurantInfoAPITest(APITestCase):
    def test_get_restaurant_info(self):
        restaurant = Restaurant.objects.create(
            name="Test Restaurant",
            address="123"
        )
        response=self.client.get('/api/restaurant-info/')
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(response.data['name'],restaurant.name)
        self.assertEqual(response.data['address'],restaurant.address)
