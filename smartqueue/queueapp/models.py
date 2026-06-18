from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Service(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Queue(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    service = models.ForeignKey(Service, on_delete=models.CASCADE)

    token_number = models.IntegerField()

    phone = models.CharField(max_length=15, default="0000000000")

    status = models.CharField(max_length=20, default="Waiting")

    created_at = models.DateTimeField(default=timezone.now)

    notified = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - Token {self.token_number}"


