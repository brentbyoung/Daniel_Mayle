from django.shortcuts import render, redirect
from django.urls import reverse
# So we can count the students in a class
from django.db.models import Count
from ..courses_app.models import Course
from ..login_reg_app.models import User
# Create your views here.
def index(request):
    context = {
        'users' : User.objects.all(),
        'courses' : Course.objects.annotate(students=Count('users')),
    }
    return render(request, 'intergration_app/index.html', context)

def create(request):
    Course.objects.add_user_to_course(request.POST)
    return redirect(reverse('intergration_index'))