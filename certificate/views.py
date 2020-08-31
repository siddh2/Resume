from django.shortcuts import render
from .models import Certificate


# Create your views here.

def all_certificate(request):
    certificates = Certificate.objects.all()
    context={
        'certificates':certificates
    }
    
    return render(request,'certificate/certificate.html', context)
