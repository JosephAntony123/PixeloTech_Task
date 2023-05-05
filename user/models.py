from django.db import models


class User(models.Model):
    mobile = models.CharField(max_length=10)
    name = models.CharField(max_length=255)
    otp = models.CharField(max_length=6)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
