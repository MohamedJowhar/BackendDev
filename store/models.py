from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.name
    

class Customer(models.Model):
    #choices
    
    
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email=models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    Date=models.DateField(null=True)
    #('database_value', 'human_readable_name')
    choices=[
        ('M','Male'),
        ('F','Female'),
     
    ]
    gender=models.CharField(max_length=1, choices=choices, null=True)
