from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def starting_page(request):
    return render(request, template_name='blog/index.html')


def posts(request):
    pass


def post_detail(request, slug):
    pass
