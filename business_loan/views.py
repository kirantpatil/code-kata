from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Company

# Create your views here.
def index(request):
    companies = Company.objects.all()
    return render(request, 'business_loan/index.html', {'companies': companies})    


  