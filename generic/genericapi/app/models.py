from django.db import models


class Student(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    mobile=models.CharField(max_length=10)
    created_at=models.DateTimeField(auto_now=True)
