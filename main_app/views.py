from django.shortcuts import render
from .models import Speciality, Doctor

# Create your views here.
def home(request):
    context = {
        'speciality': Speciality.objects.all(),
        'doctors': Doctor.objects.all()[:4]  # limit to 5
    }
    return render(request, 'main_app/home.html', context)


def doctors_list(request):
    context = {
        'doctors': Doctor.objects.all()
    }
    return render(request, 'main_app/doctors_list.html', context)   



def about(request):
    return render(request,'main_app/about.html')

def contact(request):
    return render(request,'main_app/contact.html')





