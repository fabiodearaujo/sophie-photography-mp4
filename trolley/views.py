from django.shortcuts import render

# Create your views here.

def index(request):
    """ View to connect and return the shopping trolley page """
    return render(request,'trolley/trolley.html')