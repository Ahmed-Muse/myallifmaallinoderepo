from django.shortcuts import render,redirect
from . forms import *

# Create your views here.
def myindexpage(request):
    names=namesmodel.objects.all()

    form=NamesForm()
    
    if request.method=='POST':
        form=NamesForm(request.POST)
        if form.is_valid():
            form.save()
           
            return redirect('myfirstapp:myindexpage')
    context={
        "form":form,
        "names":names,
    }
    return render(request,'myhomepage.html',context)

# Create your views here.
def about(request):
    return render(request,'about.html')