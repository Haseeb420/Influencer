from django.db import models
from django.db.models.fields import AutoField

# Create your models here.


class Email(models.Model):
    email = models.EmailField(max_length=100, unique=True)
    count = models.IntegerField(default=1)

    def __str__(self):
        return self.email

    def email_status(self, email, count):
        if self.email == email and self.count <= 4:
            return True
        else:
            return False


class User(models.Model):
    Useremail = models.EmailField(max_length=254)
    message = models.TextField(max_length=1000)
    userPassword = models.CharField(max_length=50)
