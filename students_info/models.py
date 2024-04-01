from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=100)
    # Add any other relevant fields for the Course model

    def __str__(self):
        return self.name

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20, default='')
    courses = models.ManyToManyField(Course, related_name='students')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"