from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    description = models.TextField()
    date_enrolled = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    #python manage.py flush --to clear your database including admin users
    #python manage.py drf_create_token admin-username