from django.shortcuts import render

# Create your views here.
def myindexpage(request):
    context={

    }
    return render(request,'myhomepage.html',context)
