from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    """
    index endpoint
    """
    return HttpResponse("Hello, this is the index page.")
    