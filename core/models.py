from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


# class Family(models.Model):
#     family_head = models.CharField(max_length=100)
#     village = models.CharField(max_length=100)
#     tribe_name = models.CharField(max_length=100)

#     def __str__(self):
#         return f"{self.family_head} - {self.village}"

# class Member(models.Model):
#     family = models.ForeignKey(Family, on_delete=models.CASCADE)
#     name = models.CharField(max_length=100)
#     age = models.PositiveIntegerField()
#     gender = models.CharField(max_length=10)

# class Land(models.Model):
#     family = models.ForeignKey(Family, on_delete=models.CASCADE)
#     land_area = models.FloatField()
#     land_type = models.CharField(max_length=50)  # e.g., Agricultural, Forest

# class Scheme(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.TextField()

# class SchemeBenefit(models.Model):
#     family = models.ForeignKey(Family, on_delete=models.CASCADE)
#     scheme = models.ForeignKey(Scheme, on_delete=models.CASCADE)
#     date_received = models.DateField()

class Tribe(models.Model):
    tribe=models.CharField(max_length=20,unique=True)
class Village(models.Model):
    village=models.CharField(max_length=30,unique=True)
class TribalMember(models.Model):
    phno=models.CharField(max_length=10)
    name=models.CharField(max_length=100)
    village=models.ForeignKey(Village,on_delete=models.CASCADE)
    tribe=models.ForeignKey(Tribe,on_delete=models.CASCADE,null=True, blank=True)
    gender=models.CharField(max_length=3,default='NA')
class TribeUser(models.Model):
    
    phno=models.CharField(max_length=10,unique=True)
    password=models.CharField(max_length=100)
    perm=models.BooleanField(default=False)
    # USERNAME_FIELD = 'phno'
    # REQUIRED_FIELDS = [] 
class Schemes(models.Model):
    name=models.CharField(max_length=255,unique=True)
    description=models.TextField()
    eligibility = models.TextField(blank=True, null=True)
    benefits=models.TextField(blank=True, null=True)
class MangementRoles(models.Model):
    role=models.CharField(max_length=20,unique=True)
class MangementUser(models.Model):
    name=models.CharField(max_length=100)
    phno=models.CharField(max_length=10,unique=True)
    village=models.ForeignKey(Village,on_delete=models.CASCADE,null=True,blank=True)
    role=models.ForeignKey(MangementRoles,on_delete=models.CASCADE,null=True,blank=True)

class FeedBack(models.Model):
    feedback=models.CharField(max_length=200)
    scheme=models.ForeignKey(Schemes,on_delete=models.CASCADE,null=True,blank=True)
    village=models.ForeignKey(Village,on_delete=models.CASCADE,null=True,blank=True)
    type=models.CharField(max_length=10)


'''
looks like you have pasted 
'''

