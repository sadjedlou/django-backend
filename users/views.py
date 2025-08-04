from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import USERRegistrationForm



# Create your views here.
def register(request):
    if(request.method == 'POST'):
        form = USERRegistrationForm(request.POST)  # Use the custom registration form
        if form.is_valid():
            form.save()  # Save the new user 
            username = form.cleaned_data.get('username')
            messages.success(request, f'your account has been created! You can now log in as {username}.')
            return redirect('login')  # Redirect to the blog home page after registration
        
    else:    
        form = USERRegistrationForm()
    return render(request, 'users/register.html', {'form': form})
    

