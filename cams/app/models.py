from django.db import models
from django.utils import timezone

class users(models.Model): # it stores the regiteres user
    id = models.AutoField(primary_key=True)
    username=models.CharField(max_length=150)
    password=models.TextField(max_length=20)

    def __str__(self):
        return self.username

# this table for event registration by the user
class Event(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    ]

    event_name = models.CharField(max_length=100)
    event_type = models.CharField(max_length=100)
    venue_selection = models.CharField(max_length=100)
    venue_details = models.CharField(max_length=200, blank=True, null=True)
    date_of_event = models.DateField()
    event_manager_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=10)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')


    def __str__(self):
        return self.event_name

#this is for customer support table
class HelpRequest(models.Model):
    STATUS_CHOICES = [
        ('New', 'New'),
        ('Resolved', 'Resolved'),
    ]
    username = models.CharField(max_length=100)
    email = models.EmailField()
    help_text = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='New')

    def __str__(self):
        return self.username
# this table is handeled by the administartion for registration of the manager
class Manager(models.Model):
    STATUS_CHOICES = [
        ('Available', 'Available'),
        ('Not-Available', 'Not-Available'),
    ]
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.BigIntegerField()
    is_available = models.CharField(max_length=13, choices=STATUS_CHOICES, default='Available')


    def __str__(self):
        return self.name

#this table is handeled by the administration for regitering of the venues details
class Venue(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    price=models.IntegerField()
    location=models.CharField(max_length=200)

    def __str__(self):
        return self.name