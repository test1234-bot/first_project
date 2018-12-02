from django.shortcuts import render,reverse,redirect
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("CMS首页")

def login(request):
    return HttpResponse("CMS登录页面")
