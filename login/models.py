from django.db import models


class Employees(models.Model):
     username = models.CharField(max_length=100)
     email = models.EmailField(max_length=100)
     password = models.CharField(max_length=50,default="12345678")
     phone=models.CharField(max_length=50,default='2395073221')

     def __str__(self):
         return self.username


