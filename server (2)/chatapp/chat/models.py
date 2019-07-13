from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils import timezone
from django.urls import reverse

class ChatMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField(max_length=3000)
    message_html = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):


        return self.message
