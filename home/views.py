from django.shortcuts import render

# Create your views here.

def index(request):
    """ View to connect and return the index page """
    return render(request,'home/index.html')