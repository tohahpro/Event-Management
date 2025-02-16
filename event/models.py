from django.db import models

# Create your models here.
class Participant(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

class Events(models.Model):    
    category = models.ForeignKey("Category", on_delete=models.CASCADE, default=1)
    assigned_to = models.ManyToManyField(Participant)
    name = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateField(null=True, default=True)    
    due_time = models.TimeField(null=True, default=True)
    location = models.CharField(max_length=200)

class Category(models.Model):
    CATEGORY_CHOICES = [
        ('SOCIAL', 'Social'),
        ('BUSINESS', 'Business'),
        ('PERSONAL', 'Personal')
    ]    
    category_name = models.CharField(max_length=30, choices=CATEGORY_CHOICES,default='PERSONAL')
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.category_name