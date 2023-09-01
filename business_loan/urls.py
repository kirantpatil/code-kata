from django.urls import path
from . import views

app_name = 'business_loan'

urlpatterns = [ 
               path('index', views.index, name='index')
               # path('<int:movie_id>', views.detail, name='detail')
               ]