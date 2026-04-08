from django.db import models

class User(models.Model):

    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)

    def __str__(self):
        return self.name
    
class OTP(models.Model):

    mobile = models.CharField(max_length=15)
    otp = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)    