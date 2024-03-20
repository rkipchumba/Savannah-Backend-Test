from django.db import models

# Define the Customer model
class Customer(models.Model):
    # Define fields for the Customer model
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=10, unique=True) 
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.name  # Return the name of the customer when converted to a string

# Define the Order model
class Order(models.Model):
    # Define fields for the Order model
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)  # ForeignKey relationship with Customer model
    item = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2) 
    time = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return self.item  # Return the name of the item when converted to a string
