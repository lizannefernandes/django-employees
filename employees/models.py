from django.db import models

# Create your models here.

#storing the employee data
class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    photo= models.ImageField(upload_to='images')
    designation = models.CharField(max_length=100)
    email_address = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=12, blank=True) #bank=True to make optional
    created_at = models.DateTimeField(auto_now_add=True) #auto_now_add --one time modification when it is created and saved for the first time
    updated_at = models.DateTimeField(auto_now=True) # whenever u need a feld to change the instance is saved with current time when inntance is modified

    def __str__(self):
        return(self.first_name+" "+self.last_name)


