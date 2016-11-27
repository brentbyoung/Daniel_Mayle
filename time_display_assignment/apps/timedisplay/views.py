from django.shortcuts import render
from datetime import datetime
from django.shortcuts import render, HttpResponse
# Create your views here.

def index(request):
    date = datetime.now().date().strftime('%B %-d, %Y')
    time = datetime.now().time().strftime('%-I:%M %p')
    context = {
        'datetime' : [
            {'date': date},
            {'time': time},
        ]
    }
    return render(request,'timedisplay/index.html', context)


# def index(request):
#     date = datetime.now().date().strftime('%B %-d, %Y')
#     time = datetime.now().time().strftime('%-I:%M %p')
#     context = {
#         'datetime' : [
#             {'date': date},
#             {'time': time},
#         ]
#     }