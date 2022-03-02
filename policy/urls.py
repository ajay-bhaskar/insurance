from django.urls import path

from . import views
from .views import *

app_name = 'policy'
urlpatterns = [
    path('', views.homepage, name='home'),
    path('search/', searchPolicies.as_view(), name='searchPolicies'),
    path('policySales/', views.policySales, name='policySales'),
    path('edit/<int:id>', views.editPolicy, name='editPolicy'),
    path('update/<int:id>', views.updatePolicy, name='updatePolicy'),

]
