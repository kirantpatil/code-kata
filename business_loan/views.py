from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Company, Accounting_Provider
from Accounts.Xero import FinancialStatements
from Decision_engine.service import Decision

# Create your views here.
def index(request):
    companies = Company.objects.all()
    accounts_providers = Accounting_Provider.objects.all()
    balance_sheet = FinancialStatements.BalanceSheet()
    return render(request, 'business_loan/index.html', {'companies': companies, 'accounts': accounts_providers,
                                                        'sheet': balance_sheet})    


  