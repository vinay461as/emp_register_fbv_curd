from django.db import models

# Create your models here.

class Designation(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Employee(models.Model):
    emp_code = models.CharField(max_length=5)
    fullname = models.CharField(max_length=250)
    mobile = models.CharField(max_length=15)
    email = models.EmailField()
    designation = models.ForeignKey(Designation, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.fullname
