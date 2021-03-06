from django.http import HttpResponse
from .service.service import Service
from django.views.decorators.csrf import csrf_exempt

service = Service()


def accounts_list(request):
    accounts_json = service.get_accounts_json()

    response = HttpResponse(accounts_json, content_type='application/json')
    response['Access-Control-Allow-Origin'] = '*'
    return response


def account_info(request, account_id):
    account_json = service.get_account_info_json(account_id)

    response = HttpResponse(account_json, content_type='application/json')
    response['Access-Control-Allow-Origin'] = '*'
    return response


def transactions_list(request, account_id):
    transactions_json = service.get_transactions_json(account_id)

    response = HttpResponse(transactions_json, content_type='application/json')
    response['Access-Control-Allow-Origin'] = '*'
    return response


@csrf_exempt
def put_money(request):
    service.work_with_money(request.body, 'put')

    response = HttpResponse({}, content_type='application/json')
    response['Access-Control-Allow-Origin'] = '*'
    return response


@csrf_exempt
def withdraw_money(request):
    service.work_with_money(request.body, 'withdraw')

    response = HttpResponse({}, content_type='application/json')
    response['Access-Control-Allow-Origin'] = '*'
    return response


@csrf_exempt
def close_account(request):
    service.close_account(request.body)

    response = HttpResponse({}, content_type='application/json')
    response['Access-Control-Allow-Origin'] = '*'
    return response


@csrf_exempt
def create_account(request):
    service.create_account()

    response = HttpResponse({}, content_type='application/json')
    response['Access-Control-Allow-Origin'] = '*'
    return response
