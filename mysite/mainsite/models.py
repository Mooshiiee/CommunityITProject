from django.db import models

# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    body = models.TextField()
    location_choices = [
        ('WH', 'West Haven'),
        ('ST', 'Surrounding town'),
    ]
    location = models.CharField(max_length=2, choices=location_choices)
    
    #hidden from user form
    time_created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    