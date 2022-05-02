from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse('ok')

from book.models import BookInfo
book = BookInfo(
    name = 'django',
    pub_date = '2000-1-1',
    readCount = '1'
)
book.save()