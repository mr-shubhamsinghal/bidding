from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('uname', None)
        password = request.POST.get('password', None)
        if username and password:
            user = authenticate(username=username,
                                password=password)
            if user:
                login(request, user)
                return redirect('bidding_app:get_bidding_list')
    return render(request, 'login.html')


def user_logout(request):
    logout(request)
    return redirect('bidding_app:get_bidding_list')
