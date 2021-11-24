from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    receiver = models.CharField(max_length=50)
    message = models.TextField(max_length=1000)
    subject = models.CharField(max_length=100)
    read = models.BooleanField(default=False)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.sender.username
