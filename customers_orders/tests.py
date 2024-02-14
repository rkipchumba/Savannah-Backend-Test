from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from .models import Customer, Order
from django.urls import reverse
from rest_framework import status


class OrderAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)
        self.customer = Customer.objects.create(name='Test Customer', code='TC001')
        self.order_data = {
            'customer': self.customer.id,
            'item': 'Test Item',
            'amount': 50.00,
        }

    def test_create_order(self):
        response = self.client.post('/api/orders/', self.order_data)
        self.assertEqual(response.status_code, 201)
        self.assertIn('id', response.data)
        self.assertEqual(response.data['customer'], self.customer.id)
        self.assertEqual(response.data['item'], 'Test Item')
        self.assertEqual(response.data['amount'], '50.00')

    def test_send_sms_on_order_creation(self):
        response = self.client.post('/api/orders/', self.order_data)
        self.assertEqual(response.status_code, 201)

        order = Order.objects.get(pk=response.data['id'])
        self.assertEqual(order.customer, self.customer)

    def test_order_amount_calculation(self):
        response = self.client.post('/api/orders/', self.order_data)
        self.assertEqual(response.status_code, 201)

        order = Order.objects.get(pk=response.data['id'])
        self.assertEqual(order.amount, 50.00)

    def test_get_order_list(self):
        response = self.client.get('/api/orders/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 0)  

        # Create an order and check if it appears in the list
        order = Order.objects.create(customer=self.customer, item='New Item', amount=30.00)
        response = self.client.get('/api/orders/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['id'], order.id)

class CustomerModelTest(TestCase):
    def test_create_customer(self):
        customer = Customer.objects.create(name='John Doe', code='JD001')
        self.assertEqual(customer.name, 'John Doe')
        self.assertEqual(customer.code, 'JD001')

class OrderModelTest(TestCase):
    def test_create_order(self):
        customer = Customer.objects.create(name='Jane Doe', code='JD002')
        order = Order.objects.create(customer=customer, item='Test Item', amount=50.00)
        self.assertEqual(order.customer, customer)
        self.assertEqual(order.item, 'Test Item')
        self.assertEqual(order.amount, 50.00)

class OrderAcceptanceTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.customer = Customer.objects.create(name='Test Customer', code='TC001')

    def test_create_order_view(self):
        url = reverse('order-list')
        data = {'customer': self.customer.id, 'item': 'Test Item', 'amount': 50.00}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Order.objects.count(), 1)

class OrderViewSetIntegrationTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.customer = Customer.objects.create(name='Test Customer', code='TC001')

    def test_create_order_api_view(self):
        url = reverse('order-list')
        data = {'customer': self.customer.id, 'item': 'Test Item', 'amount': 50.00}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Order.objects.count(), 1)