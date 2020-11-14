from django.urls import path
from .views import *

urlpatterns = [
    path('accounts/', accounts_list),
    path('account/<str:account_id>', account_info),
]
