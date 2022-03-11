from django import forms
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
        
    def save(self, commit=True, *args, **kwargs):
        """Save function for PasswordEntryForm"""
        pass_entry = super(CreatePasswordEntryForm, self).save(commit, *args, **kwargs)
        if pass_entry.password == None:
            pass_entry.hash_password(PasswordEntry.generate_password(), commit)
        return pass_entry
