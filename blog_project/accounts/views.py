from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from accounts.forms import MyUserCreationForm
from django.contrib import messages
from django.contrib.auth import login


def registration_view(request):
    if request.method == "POST":
        form = MyUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Регистрация прошла успешно!')
            return redirect('home')
            
        else:
            messages.error(request, 'Ваши данные некорректны!')
            
    else:
        form = MyUserCreationForm()
        
    return render(request, 'registration/registration.html', {'form':form})
            
            