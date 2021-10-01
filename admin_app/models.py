from django.db import models

# Create your models here.



class roles(models.Model):
    rolename = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True)
    is_active = models.BooleanField(default='1')
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
     return self.description

class department(models.Model):
    depname = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True)
    is_active = models.BooleanField(default='1')
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
     return self.description


class members_personalinfo(models.Model):
    role = models.ForeignKey(roles, on_delete=models.CASCADE)
    dept = models.ForeignKey(department, on_delete=models.CASCADE)
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    tel_no = models.CharField(max_length=255, unique=True)
    email = models.CharField(max_length=255, unique=True)
    address = models.CharField(max_length=255)
    is_active = models.BooleanField(default='1')
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
     return self.address

class guest_application(models.Model):
    dept = models.ForeignKey(department, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=255)
    village = models.CharField(max_length=255)
    sector = models.CharField(max_length=255, )
    district = models.CharField(max_length=255)
    tel_no = models.CharField(max_length=255,unique=True)
    nid = models.CharField(max_length=255,unique=True)
    visit_reason = models.CharField(max_length=255, blank=True)
    is_active = models.BooleanField(default='1')
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
     return self.district


class finance_info(models.Model):
    user = models.OneToOneField(members_personalinfo, on_delete=models.CASCADE,unique=True)
    paid_amount = models.CharField(max_length=255)
    balance = models.CharField(max_length=255)
    is_active = models.BooleanField(default='1')
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
     return self.balance


class attendance(models.Model):
    member = models.ForeignKey(members_personalinfo, on_delete=models.CASCADE, blank=True)
    guest = models.ForeignKey(guest_application, on_delete=models.CASCADE, blank=True)
    checkin_time = models.DateTimeField()
    checkout_time = models.DateTimeField()
    is_active = models.BooleanField(default='1')
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
     return self.checkin_time


class users(models.Model):
    user = models.OneToOneField(members_personalinfo, on_delete=models.CASCADE,unique=True)
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255 )
    is_active = models.BooleanField(default='1')
    date_joined = models.DateTimeField(auto_now_add=True)
    def __str__(self):
     return self.password


