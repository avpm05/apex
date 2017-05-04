from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from    django.shortcuts import render,reverse
from .forms import SendOrder
from django.core.mail   import send_mail
# Create your views here.

def index(request):
    sent = False
    if request.method=='POST':
        form=SendOrder(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            subject = 'New order'
            message = 'Name customer ' + cd['name']
            send_mail(subject, message, cd['email'],  ['mail@apexconsult.ru'])
            HttpResponseRedirect(reverse(index))
            sent=True
    else:
        form=SendOrder()

    return render(request,'main.html',{'form':form,'sent':sent})

