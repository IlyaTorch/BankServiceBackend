from django.http import HttpResponse
from .service.service import Service


service = Service()


def accounts_list(request):
    accounts_json = service.get_accounts_json()

    response = HttpResponse(accounts_json, content_type='application/json')
    response['Access-Control-Allow-Origin'] = '*'
    return response
