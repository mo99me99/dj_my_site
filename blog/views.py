from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def starting_page(request):
    return HttpResponse('Hello this is index page')


def posts(request):
    pass


def post_detail(request, slug):
    pass
