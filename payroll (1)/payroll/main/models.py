from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class EmployeeDetail(models.Model):
    empid = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=12, null=True)
    address1 = models.TextField(null=True)
    address2 = models.TextField(null=True)
    address3 = models.TextField(null=True)
    designation = models.CharField(max_length=50 , null=True)
    joiningdate = models.DateField(null=True)
    basicpay = models.CharField(max_length=15, null=True)


class SalaryDetail(models.Model):
    salid = models.AutoField(primary_key=True)
    empid = models.ForeignKey(EmployeeDetail, on_delete=models.CASCADE)
    hra = models.CharField(max_length=20)
    da = models.CharField(max_length=20)
    com = models.CharField(max_length=20)
    ma = models.CharField(max_length=20)
    gt = models.CharField(max_length=20)
    it = models.CharField(max_length=20)
    pt = models.CharField(max_length=20)
    ins = models.CharField(max_length=20)
    work = models.CharField(max_length=20 , null=True)
    present = models.CharField(max_length=20, null=True)
    net = models.CharField(max_length=20)
    


class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('employee', 'Employee'),
        ('hr', 'HR'),
        ('clerk', 'Clerk'),
        
    ]

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='employee')

    def __str__(self):
        return self.username  

