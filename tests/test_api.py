from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.test import TestCase
from apps.customer.models import Customer

User = get_user_model()


class TestApiDrf(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.password = 'master123'
        cls.customer = Customer.objects.create_customer(
            'customer_test@test.net',
            'Pytest Admin',
            '123,456',
            cls.password,
        )
        cls.client = APIClient()

        # Getting the tokens
        url = reverse('token_obtain_pair')
        data = {
           'email': cls.customer.email,
           'password': cls.password
        }
        response = cls.client.post(url, data=data)
        cls.tokens = response.data

    # Create a customer
    def test_create_customer(self):
        url = reverse('api-root:addcustomer-list')
        data = {
            "full_name": "Loan Schneider",
            "phones": "123456",
            "email": "loan@fakemail.com",
            "password": "change-me"
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # creating an address for the user-created above
    def test_create_address(self):
        url = reverse('api-root:address-list')
        data = {
          "customer": self.customer.id,
          "street": "Rua Estácio",
          "number": "568",
          "country": "BR",
          "zip": "0987654",
          "address_type": "B"
        }
        auth = 'Bearer {0}'.format(self.tokens['access'])
        response = self.client.post(url, data, HTTP_AUTHORIZATION=auth)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    #  Adding a stock item
    def test_creating_item(self):
        url = reverse('api-root:itens-list')
        data = {
          "sku": "sku-123",
          "name": "Alkingel70",
          "description": "Alcool em gel 70",
          "bar_code": "123456",
          "price": "5.80"
        }

        auth = 'Bearer {0}'.format(self.tokens['access'])
        response = self.client.post(url, data, HTTP_AUTHORIZATION=auth)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
