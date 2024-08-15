from django.shortcuts import render, redirect
from django.contrib import messages
from contact.forms import RegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth


def register(request):
    form = RegisterForm()

    context = {
        'form': form
    }

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'User registered successfully.')
            return redirect('contact:login')

    return render(request, 'contact/register.html', context)


def login_view(request):
    form = AuthenticationForm(request)

    context = {
        'form': form
    }

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            messages.success(request, 'User logged in successfully.')
            return redirect('contact:index')

        messages.error(request, 'Invalid login.')

    return render(request, 'contact/login.html', context)


def logout_view(request):
    auth.logout(request)
    return redirect('contact:login')
