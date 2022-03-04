from django.shortcuts import render, redirect
from passwords.forms import CreatePasswordEntryForm

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



