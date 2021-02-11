from django.db import models
from backend.mixin import TimeStampedModel
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.crypto import get_random_string
from djchoices import DjangoChoices, ChoiceItem
import uuid


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


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


def get_random_6():
    return get_random_string(length=6)


class Code(TimeStampedModel):
    class StatusType(DjangoChoices):
        published = ChoiceItem(label='Published', value='published')
        unpublished = ChoiceItem(label='Unpublished', value='unpublished')

    status = models.CharField(verbose_name='Status',
                              max_length=30,
                              choices=StatusType.choices,
                              default=StatusType.published)
    name = models.CharField(verbose_name='Name', max_length=255)
    code = models.CharField(verbose_name='Code', max_length=10, default=get_random_6, blank=True, null=True)
    min_price = models.IntegerField(verbose_name='Min price')
    discount = models.IntegerField(verbose_name='Discount')
    count = models.IntegerField(verbose_name='Count code')

    def __str__(self):
        return self.name

    def count_use_code(self):
        return self.usecode_set.count()

    class Meta:
        verbose_name = 'Code'
        verbose_name_plural = 'Codes'


class UseCode(TimeStampedModel):
    code = models.ForeignKey(Code, verbose_name='Guest', on_delete=models.CASCADE, blank=True, null=True)
    guest = models.ForeignKey(Guest, verbose_name='Guest', on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE, blank=True, null=True)
