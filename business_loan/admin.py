from django.contrib import admin
from .models import Company, Accounting_Provider


class CompanyAdmin(admin.ModelAdmin):
    exclude = ('date_created', )
    list_display = ('name',  'incorporation_year')
    
class Accounting_ProviderAdmin(admin.ModelAdmin):
    list_display = ('name',)
    
admin.site.register(Company, CompanyAdmin)
admin.site.register(Accounting_Provider, Accounting_ProviderAdmin)
