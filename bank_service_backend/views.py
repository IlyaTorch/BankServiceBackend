from django.shortcuts import redirect


def redirect_bank(request):
    return redirect('accounts_list', permanent=True)
