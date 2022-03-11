from django import forms
from passwords.models import PasswordEntry
from passwords.password_generator import generate_password_advanced


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

        # TODO: Change functionality to allow for passwords to be "rerolled"
        if pass_entry.password is None:
            pass_entry.hash_password(generate_password_advanced(), commit)
        return pass_entry
