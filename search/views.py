from django.shortcuts import render
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger


# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import Company
from  django.views.generic import ListView




from django.shortcuts import render

# Create your views here.
def apexsearch(request):
    return HttpResponse("Search")

def company_list(request):
    object_list = Company.objects.all()
    paginator = Paginator(object_list,50)
    page = request.GET.get('page')

    try:
        companies = paginator.page('page')
    except PageNotAnInteger:
        companies = paginator.page(1)
    except EmptyPage:
        companies = paginator.page(paginator.num_pages)
    return render(request,'Search.html',{'page':page,'companies':companies})

class CompaniesListView(ListView):
    queryset = Company.objects.all()
    context_object_name = 'companies'
    paginate_by = 100
    template_name = 'Search.html'
