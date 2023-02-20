from django.shortcuts import render

# Create your views here.

def index(response, *args, **kwargs):
    return render(response, 'userInterface/index.html', {})