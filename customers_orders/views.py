from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
import africastalking 
from django.conf import settings
from django.utils.html import escape

from rest_framework import serializers, viewsets
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

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    # permission_classes = [IsAuthenticated]

    def perform_destroy(self, instance):
        try:
            print("Deleting order...")
            instance.delete()
            print("Order deleted successfully.")
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            print(f"Error deleting order: {e}")
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def perform_create(self, serializer):
        super().perform_create(serializer)
        
        # Send SMS alert
        order = serializer.instance
        customer = order.customer
        message = f"Dear {customer.name}, your order with item {order.item} has been added successfully. Total amount is {order.amount}"
        self.send_sms(customer.code, message)

    def send_sms(self, phone_number, message):
        africastalking.initialize(settings.USERNAME, settings.API_KEY)
        sms = africastalking.SMS 

        recipients = [f"+{254728521615}"] 
        sender = 'M-Savannah' 
        escaped_message = escape(message)  # encode data before being rendered in the HTML
        response = sms.send(message, recipients, sender)
        print(response)
