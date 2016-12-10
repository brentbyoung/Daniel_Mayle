from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from models import User
# Create your views here.
def index(request):
    return render(request, 'login_reg_app/index.html')

def login(request):
    result = User.objects.validateLogin(request)

    if result[0] == False:
        print_messages(request, result[1])
        return redirect(reverse('users_index'))

    return log_user_in(request, result[1])

def register(request):
    result = User.objects.validateReg(request)

    if result[0] == False:
        print_messages(request, result[1])
        return redirect(reverse('users_index'))

    return log_user_in(request, result[1])

def success(request):
    if not 'user' in request.session:
        return redirect(reverse('users_index'))
    return render(request, 'login_reg_app/success.html')

def print_messages(request, message_list):
    for message in message_list:
        messages.add_message(request, messages.INFO, message)

def log_user_in(request, user):
    request.session['user'] = {
        'id' : user.id,
        'first_name' : user.first_name,
        'last_name' : user.last_name,
        'email' : user.email,
    }
    return redirect(reverse('users_success'))

def logout(request):
    request.session.pop('user')
    return redirect(reverse('users_index'))