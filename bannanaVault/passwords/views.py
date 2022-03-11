from ast import Pass
from django.shortcuts import render, redirect
from django.http import Http404

from passwords.forms import CreatePasswordEntryForm
from passwords.models import PasswordEntry

# Create your views here.
def create_password_entry(request):
    """"""
    
    if request.method == 'POST':
        form = CreatePasswordEntryForm(data=request.POST)
        if form.is_valid():
            pass_entry = form.save(commit=False)
            pass_entry.user = request.user
            pass_entry.vault = request.user.password_vault
            password = pass_entry.generate_password()
            pass_entry.hash_password(password)
            pass_entry.save()
            return redirect('home')
    else:
        form = CreatePasswordEntryForm()
    
    return render(request, 'passwords/create_password_entry.html', context={'form': form})

def delete_password_entry(request, pk):
    try:
        pass_entry = PasswordEntry.objects.get(pk=pk)
        pass_entry.delete()
    except:
        raise Http404('This Password Entry does not exit')
    return redirect('home')