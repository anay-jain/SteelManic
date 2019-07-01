from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    response =" Hello world"
    # return render(request,'mainview/index.html')
    return HttpResponse(response)

# Create your views here.
