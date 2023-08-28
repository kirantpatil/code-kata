from django import forms
from django.forms import ModelForm, Select, TextInput, ModelChoiceField
from business_loan.models import Company, Accounting_Provider


company_set = Company.objects.all()
account_set = Accounting_Provider.objects.all()
    
class UserForm(forms.Form):
    company_name = forms.ModelChoiceField(
            widget=forms.Select,
            queryset=company_set
        )
    accounting_provider = forms.ModelChoiceField(
        widget=forms.Select,
        queryset=account_set
    )
    loan_amount= forms.CharField(max_length=100)
    
    
