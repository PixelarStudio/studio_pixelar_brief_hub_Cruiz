# briefs/forms.py
from django import forms
from .models import Brief

class BriefForm(forms.ModelForm):
    class Meta:
        model = Brief
        fields = ["title", "client_name", "service_type", "body", "reference_image"]
