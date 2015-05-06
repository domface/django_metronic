# from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.generic import TemplateView
import json
from django.http import JsonResponse


from django.contrib.auth.models import User
from django.contrib.auth import authenticate

# Create your views here.

class MetronicAdmin(TemplateView):
    template_name = 'metronic_index.html'

def index(request):
    args = {'value':'IT WORKS'}
    return render_to_response('metronic_index.html', args)

def json_test(request):

    user = authenticate(username='john', password='johnpassword')
    user = request.user.username
    if user:
        json_response  ={'result':'welcome guest'}
    else:
        json_response = {'result':user}
    json_response = {'result':str(request.user)}
    return JsonResponse(json_response)

def login_test(request):
    username = request.GET.get('username', '')
    password = request.GET.get('password', '')
    user = authenticate(username=username, password=password)
    args = {'result':username}
    return JsonResponse(args)

