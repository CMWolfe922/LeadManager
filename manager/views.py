from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone as tz
from django.contrib.auth.views import LoginView, LogoutView
from allauth.socialaccount.views import SocialAccount

# Create your views here.
def index(request):
    return render(request, 'index.html',context={})

