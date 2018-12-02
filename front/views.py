from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.template.loader import render_to_string


# Create your views here.


def index(request):
    username = request.GET.get('username')
    if username:
        return HttpResponse("前台首页")
    else:
        login_url = reverse('front:login')
        return redirect(login_url)


def login(request):
    return HttpResponse("前台登录页面")


def test_temp(request):
    # html = render_to_string("index.html")
    return render(request, 'index.html')
