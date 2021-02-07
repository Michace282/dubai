from django.db import models
from backend.mixin import TimeStampedModel
import uuid


class Guest(TimeStampedModel):
    uuid = models.UUIDField(verbose_name='UUID', default=uuid.uuid4, unique=True)


class Subscribe(TimeStampedModel):
    email = models.EmailField(verbose_name='E-Mail')

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Subscribe'
        verbose_name_plural = 'Subscribes'


class Contact(TimeStampedModel):
    email_or_phone = models.CharField(verbose_name='E-Mail or Phone', max_length=255)
    name = models.CharField(verbose_name='Name', max_length=255, blank=True, null=True)
    text = models.TextField(verbose_name='Text', blank=True, null=True)

    def __str__(self):
        return self.email_or_phone

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'
