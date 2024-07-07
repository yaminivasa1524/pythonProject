from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return render(request,'home1.html')
def help(request):
    return HttpResponse("<h5>Hiii</h5>")
# Create your views here.
