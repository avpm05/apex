from django.http import HttpResponse
from django.template import loader
from    django.shortcuts import render
from .forms import SendOrder
from django.core.mail   import send_mail
# Create your views here.

def index(request):
    if request.method=='POST':
        form=SendOrder(request.POST)
        if form.is_valid():
            cd = form.cleaned_data

    else:
        form=SendOrder()


    return render(request,'main.html',{'form':form})

