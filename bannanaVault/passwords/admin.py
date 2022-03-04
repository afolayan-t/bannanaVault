from django.contrib import admin
from passwords.models import PasswordEntry, PasswordVault
# Register your models here.

admin.site.register(PasswordVault)
admin.site.register(PasswordEntry)
