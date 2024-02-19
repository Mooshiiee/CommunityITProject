from django.db import models

# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    body = models.TextField()
    location_choices = [
        ('WH', 'West Haven'),
        ('MF', 'Milford'),
        ('OR', 'Orange'),
        ('HD', 'Hamden'),
        ('NH', 'New Haven'), 
        ('NA', 'Other'),
    ]
    location = models.CharField(max_length=2, choices=location_choices)
    
    #hidden from user form
    time_created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Classes(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    time = models.DateTimeField(auto_now=False, auto_now_add=False)
    town = models.CharField(max_length=50)
    availability = models.CharField(max_length=50)
    descritption = models.TextField()
    
    def __str__(self):
        return f"{self.name} {self.availability}"