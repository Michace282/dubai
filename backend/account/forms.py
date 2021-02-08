from django.forms import ModelForm
from .models import Subscribe, Contact, Guest, Profile


class SubscribeForm(ModelForm):
    class Meta:
        model = Subscribe
        fields = ['email']


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['email_or_phone', 'name', 'text']
