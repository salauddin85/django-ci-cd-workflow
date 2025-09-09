from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Item

class ItemAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.item_data = {
            "name": "Test Item",
            "description": "This is a test item",
            "price": "99.99"
        }

    def test_create_item(self):
        response = self.client.post("/api/items/", self.item_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Item.objects.count(), 1)
        self.assertEqual(Item.objects.get().name, "Test Item")

    def test_get_items(self):
        # Create an item first
        Item.objects.create(**self.item_data)
        response = self.client.get("/api/items/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["names"], "Test Item")
