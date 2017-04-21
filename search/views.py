from django.shortcuts import render


# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import Company




from django.shortcuts import render

# Create your views here.
def apexsearch(request):


    return HttpResponse("Search")

def company_list(request):
    companies = Company.objects.all()[:1000]
    return render(request, 'Search.html', {'companies':companies})