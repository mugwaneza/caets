from django.db import models

# Create your models here.
import datetime
from django.utils import timezone


class visitor_chat(models.Model):
    names = models.CharField(max_length=255, blank=False)
    email = models.CharField(max_length=255, blank=False)
    created_at = models.DateTimeField(("created_at"), default=timezone.now() )
    def __str__(self):
     return self.email

class visitor_chat_message(models.Model):
    posted_by_id = models.ForeignKey(visitor_chat, on_delete=models.CASCADE)
    encrypted_message = models.CharField(max_length=1024, blank=False, default='')
    encrypted_replay = models.CharField(max_length=1024, blank=True, default='')
    encrypted_file_path = models.CharField(max_length=3032, blank=False,  default='')
    is_read = models.BooleanField(default='0')
    replied_at = models.CharField( max_length=255, blank=True,  default='')
    created_at = models.DateTimeField(("created_at"), default=timezone.now())
    def __str__(self):
     return self.created_at

class chat_keys(models.Model):
    visitor_chat_message_id = models.ForeignKey(visitor_chat_message, on_delete=models.CASCADE)
    public_keypath = models.CharField(max_length=255, blank=False)
    privatekey_path = models.CharField(max_length=255, blank=False)
    pass_phrase = models.CharField(max_length=255, blank=False)
    created_at = models.DateTimeField(("Created_at"), default=timezone.now())

    def __str__(self):
     return self.public_keypath



