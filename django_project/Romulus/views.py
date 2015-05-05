# from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.generic import TemplateView

# Create your views here.

class MetronicAdmin(TemplateView):
    template_name = 'metronic_index.html'

def test(request):
    return HttpResponse("<h1>Project Romulus</h1><br><p>under construction...</p>")
def index(request):
    return render_to_response('metronic_index.html')