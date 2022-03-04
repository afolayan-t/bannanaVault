from django import forms
from django.contrib.auth.models import User
from passwords.models import PasswordEntry


class CreatePasswordEntryForm(forms.ModelForm):
    """Form that will be used to create passwor entries"""

    class Meta:
        model = PasswordEntry
        fields = [
            'site_name',
            'site_url',
            'auth_id'
        ]
        
