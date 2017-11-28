from django.http import HttpResponse
from django.shortcuts import render_to_response
def hello(request):
    return HttpResponse("hello world!")
def page_not_found(request):
    return render_to_response('404.html')