from django.db import models

# Create your models here.
#creating company model
class Company(models.Model):
    comapany_id = models.AutoField(primary_key= True)
    name = models.CharField(max_length = 50)
    location = models.CharField(max_length = 50)
    about = models.TextField()
    type = models.CharField(max_length = 100, choices =
    (('IT','IT'),('Non IT','Non IT'),('mobile phones','mobile phones')))
    added_date = models.DateTimeField(auto_now = True)
    active = models.BooleanField(default = True) 
    def __str__(self):
        return f"{self.name} -- {self.location}"


class Employee(models.Model):
    name = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100)
    address = models.CharField(max_length = 200)
    phone= models.CharField(max_length = 10)
    about = models.TextField()
    position = models.CharField(max_length = 100, choices = (
        ('Manager', 'manager'),
        ('Software Developer',"sd"),
        ("Project Leader" , "pl")
    ))
    company = models.ForeignKey(Company, on_delete = models.CASCADE)
