from django import forms
from django.contrib.auth.models import User
from .models import Message

class MessageForm(forms.ModelForm):
    recipient = forms.ModelChoiceField(
        queryset=User.objects.all(),
        label="Destinatario",
    )

    class Meta:
        model = Message
        fields = ["recipient", "subject", "body"]
