from django.urls import path
from .views import *

urlpatterns = [
    path('accounts/', accounts_list, name='accounts_list'),
    path('accounts/<str:account_id>', account_info),
    path('transactions/<str:account_id>', transactions_list),
    path('put-money/', put_money),
    path('withdraw-money/', withdraw_money),
    path('close-account/', close_account),
]
