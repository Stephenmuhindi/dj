from django.contrib.auth.models import User
from django.db import models

from khejas.models import Khejas

class Conversations(models.Model):
    khejas = models.ForeignKey(Khejas, related_name='conversations', on_delete=models.CASCADE)
    members = models.ManyToManyField(User, related_name='conversations')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-modified_at',)
    
class ConversationsMessage(models.Model):
    conversations = models.ForeignKey(Conversations, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='created_messages', on_delete=models.CASCADE)