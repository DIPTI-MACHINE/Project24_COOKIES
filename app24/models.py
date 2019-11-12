from django.db import models

class EmployeeModel(models.Model):
    eid = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=100,unique=True)
    password = models.CharField(max_length=100)
    image = models.ImageField(upload_to="emp_images/")
