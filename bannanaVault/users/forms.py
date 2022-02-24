from django import forms
from string import punctuation

from users.models import UserProfile

punctuation = r"""!"#$%&"()*+,/:;<=>?@[\]^`{|}~"""

class SignupForm(forms.ModelForm):
    username = forms.CharField(label="Username", max_length=15)
    email_address = forms.CharField(label="email", max_length=15)
    first_name = forms.CharField(label="First Name", max_length=20)
    last_name = forms.CharField(label="Last Name", max_length=20)
    password = forms.CharField(label="Password", max_length=50, widget=forms.PasswordInput)
    confirm_password = forms.CharField(label="Confirm Password", max_length=50, widget=forms.PasswordInput)
    profile_picture = forms.ImageField()

    class Meta:
        model = UserProfile
        fields = [
            'username',
            'email_address',
            'first_name',
            'last_name',
            'password',
            'confirm_password',
            'profile_picture'
        ]
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

    def clean_username(self):
        username = self.cleaned_data["username"]
        if punctuation in username:
            raise forms.ValidationError("Please Remove Special Characters")
        else:
            return username

    def clean_email_address(self):
        email = self.cleaned_data["email_address"]
        return email.lower()

    def clean_confirm_password(self):
        password = self.cleaned_data["password"]
        confirm_password = self.cleaned_data["confirm_password"]
        if password and confirm_password and password == confirm_password:
            if confirm_password >= 7:
                return confirm_password
            else:
                raise forms.ValidationError("Your Password must be atleast 7 characters.")
        else:
            raise forms.ValidationError("Your password doesn't match")


