from django.shortcuts import render, redirect
import random
# Create your views here.
def index(request):
    return render(request,'ninja_app/index.html')

def show(request, ninja_color):
    turtle_options = {
        'red':'ninja_app/images/raphael.jpg',
        'blue':'ninja_app/images/leonardo.jpg',
        'orange':'ninja_app/images/michelangelo.jpg',
        'purple':'ninja_app/images/donatello.jpg'
    }
    if ninja_color in turtle_options:
        context = {
            'image':turtle_options[ninja_color]
        }
    else:
        context = {
            'image':'ninja_app/images/notapril.jpg'
        }
    
    return render(request,'ninja_app/index.html',context)

def noshow(request):
	return render(request, 'ninja_app/no_show.html')