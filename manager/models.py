from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, permission_required
from django.db.utils import timezone


# Create your models here.
class Employee(models.Model):
    employee = models.ForeignKey(User, related_name='employee', on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True, name="created")
    
    class Meta:
        permissions = (
            'can_create_customer', "Can create customer data",
            'can_create_orders', "Can create customer orders",
            'can_create_employee', "Can create employee data",
            'can_edit_employee', "Can edit employee data",
            'can_delete_employee', "Can delete employee data",
            'can_delete_customer', "Can delete customer data",
            'can_edit_customer', "can edit customer data",
            'can_update_order', "Can update customer order",
            'can_close_order', "Can close customer order",
        )
    
class Customer(models.Model):
    customer = models.ForeignKey(User, related_name='customer', on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True, name="created")
    
    class Meta:
        permissions = (
            'can_view_customer_orders', 'Can view list of customers orders',
            'can_edit_order','Can edit their order',
            'can_update_profile', 'can update customer profile',
            'can_place_order', 'customer can place a new order',
        )