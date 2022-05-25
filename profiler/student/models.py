from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Faculty(models.Model):
  first_name= models.CharField(max_length=15)
  last_name= models.CharField(max_length=15)
  username= models.CharField( max_length=50)
  password=models.CharField( max_length=15)
  email =models.EmailField( max_length=254)
  
  def __str__(self):
      return self.first_name
  
class student_profile(models.Model):
  full_name=models.CharField( max_length=50,default="")
  Roll_no=models.CharField(max_length=10,unique=True)
  mobile_no=models.BigIntegerField(null=True)
  address=models.CharField( max_length=100,null=True)
  birthdate = models.DateField(blank=True, null=True ) 
  image=models.ImageField( upload_to="student/images", height_field=None, width_field=None, max_length=None,default="")
  # clas=models.TextField(max_length=50)
  # dept=models.TextField(max_length=50,default="")
  mentor=models.TextField(max_length=50,default="",null=True)
  travel=models.IntegerField(default="")
  maths=models.FloatField(default=00.00)
  algo=models.FloatField(default=00.00)
  operating=models.FloatField(default=00.00)
  micro=models.FloatField(default=00.00)
  dbms=models.FloatField(default=00.00)
  cgpa=models.CharField(max_length=10,default="")
  attendence=models.FloatField(default=00.00)
  bloodgroup=models.CharField( max_length=5,default='O+')
  language=models.TextField(max_length=50,default="")
  internship=models.TextField(max_length=50,default="")
  health=models.TextField(default="")
  familymember=models.IntegerField(default=0)
  annualin=models.CharField(max_length=12,default=0)
  areaofinterest=models.TextField(max_length=50,default="")
  fatheroccupation=models.TextField(max_length=50,default="")
  connect=models.ForeignKey(User, blank=True,null=True, on_delete=models.CASCADE)
  
  def __str__(self):
    return str(self.Roll_no)

  