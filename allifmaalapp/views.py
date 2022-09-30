from turtle import title
from django.shortcuts import render, redirect,get_object_or_404
from .models import *
from .forms import *
from django.contrib import messages
from uuid import uuid4
from django.http.response import HttpResponse, JsonResponse

from django.http.response import HttpResponse, JsonResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
# Create your views here.
def allifmaalmaindashboard(request):
    context={

    }
    return render(request,'allifmaalapp/dashboard/allifmaaldashboard.html',context)

