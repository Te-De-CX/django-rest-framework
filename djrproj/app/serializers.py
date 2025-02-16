from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = {
            'name','age'
        }
# Compare this snippet from djrproj/app/urls.py:
# """
# URL configuration for app application.