
from django.shortcuts import render
from forms import UserForm
from Accounts.Xero import FinancialStatements
from Rules_engine.rules import PreAssessment
from Decision_engine.service import Decision


def home(request):
    return render(request, 'home.html')


def index(request):
    submitbutton= request.POST.get("submit")

    company_name=''
    account_provider=''
    loan_amount=''
    balance_sheet=''
    preAssessment = ''
    avg_assetvalue= ''
    decision = ''

    form= UserForm(request.POST or None)
    if form.is_valid():
        company_name= form.cleaned_data.get("company_name")
        account_provider = form.cleaned_data.get("accounting_provider")
        loan_amount = form.cleaned_data.get("loan_amount")
        
    if company_name:
        company_name = str(company_name)
        balance_sheet = FinancialStatements.BalanceSheet(company_name)
        preAssessment,avg_assetvalue = PreAssessment.get_preassessment(balance_sheet, loan_amount)
        decision = Decision.check_status(company_name, preAssessment, balance_sheet)
            
    
    context = {'form': form, 'company_name': company_name, 'accounting_provider':account_provider,
              'submitbutton': submitbutton, 'loan_amount':loan_amount, 'balance_sheet':balance_sheet, 
              'preAssessment':preAssessment, 'average_assetvalue':avg_assetvalue, 'decision': decision}
    
    return render(request, 'index.html', context)

    #return render(request, 'business_loan/index.html', {'companies': company_name, 'accounts': account_provider,
    #                                                    'sheet': balance_sheet})    
