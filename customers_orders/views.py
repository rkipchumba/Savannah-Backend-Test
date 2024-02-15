from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework import serializers, viewsets, status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from django.conf import settings
from django.utils.html import escape
import africastalking

from .models import Customer, Order

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'name', 'code']

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'customer', 'item', 'amount', 'time']

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    # permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        # Check if the provided code already exists
        code = request.data.get('code')
        existing_customer = Customer.objects.filter(code=code).first()

        if existing_customer:
            error_message = f"Customer with the code '{code}' already exists."
            raise ValidationError({"code": [error_message]})

        # Continue with the normal creation process
        return super().create(request, *args, **kwargs)

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    # permission_classes = [IsAuthenticated]


    def perform_create(self, serializer):
        super().perform_create(serializer)
        
        # Send SMS alert
        order = serializer.instance
        customer = order.customer
        order_time = order.time.strftime('%Y-%m-%d %H:%M')
        message = f"Dear {customer.name}, your order with item {order.item} has been added successfully on {order_time}. Total amount is {order.amount}."
        self.send_sms(customer.code, message)

    def send_sms(self, phone_number, message):
        africastalking.initialize(settings.USERNAME, settings.API_KEY)
        sms = africastalking.SMS 

        recipients = [f"+{254728521615}"] 
        sender = 'M-Savannah' 
        escaped_message = escape(message)  # encode data before being rendered in the HTML
        response = sms.send(message, recipients, sender)
        print(response)
