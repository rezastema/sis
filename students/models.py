from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=255)
    student_id = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')])
    address = models.TextField()

    def __str__(self):
        return f"{self.student_id} - {self.name}"
