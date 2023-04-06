from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=20, unique=True, primary_key=True)
    email = models.EmailField()
    

class Library(models.Model):
    book_id = models.IntegerField(unique=True)
    book_name = models.CharField(max_length=100)
    writer = models.CharField(max_length=100)
    quantity = models.IntegerField()
   
