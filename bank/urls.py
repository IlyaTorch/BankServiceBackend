from django.urls import path
from .views import *

urlpatterns = [
    path('accounts/', accounts_list),
    path('accounts/<str:account_id>', account_info),
    path('transactions/<str:account_id>', transactions_list),
]
