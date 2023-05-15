# Create your views here.
from datetime import datetime

from django.http.response import HttpResponse


def health(request):
    return HttpResponse(f'OK - {datetime.now()}')
