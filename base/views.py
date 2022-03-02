from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def taskList(request):
    return HttpResponse("<h2>Task List </h2>") 