import os
import logging
import africastalking
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError
from datetime import datetime

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from django.contrib.auth.models import AnonymousUser

from django.conf import settings
from .models import Customer, Order
from .serializers import CustomerSerializer, OrderSerializer

from dotenv import load_dotenv
load_dotenv('.env')

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    # create method to handle the creation of new customers
    def create(self, request, *args, **kwargs):
        # Check if the user is authenticated
        if not request.user or isinstance(request.user, AnonymousUser):
            return self.handle_unauthenticated_user()

        code = request.data.get('code')
        phone_number = request.data.get('phone_number') 
        existing_customer = Customer.objects.filter(code=code).first()

        if existing_customer:
            error_message = f"Customer with the code '{code}' already exists."
            raise ValidationError({"code": [error_message]})
            
        return super().create(request, *args, **kwargs)

    def handle_unauthenticated_user(self):
        # Handle unauthenticated user gracefully
        return Response(
            {"detail": "Authentication credentials were not provided."},
            status=status.HTTP_401_UNAUTHORIZED
        )


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        super().perform_create(serializer)
        order = serializer.instance
        customer = order.customer
        current_time = datetime.now()
        order_time = current_time.strftime('%Y-%m-%d %H:%M')
        message = f"Dear {customer.name}, your order with item {order.item} has been added successfully on {order_time}. Total amount is Ksh {order.amount}."
        phone_number = customer.phone_number
        self.send_sms(phone_number, message)

    def send_sms(self, phone_number, message):
        africastalking.initialize(os.getenv('AFRICASTAKING_USERNAME'), os.getenv('AFRICASTAKING_API_KEY'))
        sms = africastalking.SMS


        try:
            # Check if the phone number includes the country code
            if not phone_number.startswith('+'):
                raise ValueError("Phone number must include the country code (e.g., +254 for Kenya)")

            # Attempt to send SMS
            recipients = [f"{phone_number}"]
            sender = 'M-Savannah' 
            response = sms.send(message, recipients, sender)

            # Check response for success and handle accordingly
            if response['SMSMessageData']['Recipients'][0]['status'] == 'Success':
                logging.info("SMS sent successfully!")
            else:
                logging.error("Failed to send SMS. Check Africastalking response: %s", response)

        except ValueError as e:
            # Handle the ValueError (Invalid phone number) gracefully
            logging.error("Error sending SMS: %s", e)


