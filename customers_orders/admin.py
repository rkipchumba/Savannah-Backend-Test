from django.contrib import admin
from .models import Customer, Order

# Register the Customer model
admin.site.register(Customer)

# Register the Order model
admin.site.register(Order)
