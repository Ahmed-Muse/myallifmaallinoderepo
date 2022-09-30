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


##################################33 our customers ###################################3
def allifmaalcustomers(request):
    title="Allifmaal Customers"
    customers=AllifmaalCustomersModel.objects.all()
    form=AddAllifmaalCustomerForm()
    
    if request.method == 'POST':
        form=AddAllifmaalCustomerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            
            return redirect('allifmaalapp:allifmaalcustomers')
    else:
        form=AddAllifmaalCustomerForm()
    context={
        
        "form":form,
        "title":title,
        
        "customers":customers,
    }

   
    return render(request,'allifmaalapp/customers/allifmaal-customers-list.html',context)

def show_allifmaal_customer_details(request,pk):
    title="Customer Details"
    try:
        customer_detail=AllifmaalCustomersModel.objects.get(id=pk)
    except:
        messages.error(request, 'Something went wrong')
        return redirect('allifmaalapp:allifmaalcustomers')

    context={
        "customer_detail":customer_detail,
        "title":title,

    }
    return render(request,'allifmaalapp/customers/allifmaal-customers-details.html',context)


def delete_allifmaal_customer(request,pk):
    try:
        AllifmaalCustomersModel.objects.get(id=pk).delete()
    except:
        messages.error(request, 'Something went wrong')
        return redirect('allifmaalapp:allifmaalcustomers')

    return redirect('allifmaalapp:allifmaalcustomers')

def update_allifmaal_customer(request,pk):
    title="Update Customer Details"
    update= AllifmaalCustomersModel.objects.get(id=pk)
    form = AddAllifmaalCustomerForm(instance=update)
   
    if request.method == 'POST':
        form = AddAllifmaalCustomerForm(request.POST, instance=update)
        if form.is_valid():
            form.save()
          
            return redirect('allifmaalapp:allifmaalcustomers')

    context = {
		'form':form,
        "update":update,
        "title":title,
    }
    
    return render(request,'allifmaalapp/customers/allifmaal-customers-list.html',context)

def AllifmaaltopUpCustomerAccount(request,pk):
    

    global customer,mycustid
    
    try:
        customer=AllifmaalCustomersModel.objects.get(id=pk)#very important to get id to go to particular shipment
        initial_balance=customer.balance#this gives the initial account
        mycustid=customer.id
        title="To Up For "+ str(customer)
    except:
        return HttpResponse("Sorry there is a problem ! ")
    
    
    form=AddAllifmaalCustomerPaymentForm()
    top_up_cust_account= get_object_or_404(AllifmaalCustomersModel, id=pk)


    topups= AllifmaalCustomerPaymentsModel.objects.filter(customer=customer)#this line helps to
    
    cust_acc_total = 0.0
    if len(topups) > 0:
        for payment in topups:
            amount= float(payment.amount) 
            cust_acc_total += amount

    
    add_item= None
    if request.method == 'POST':
        form=AddAllifmaalCustomerPaymentForm(request.POST)
        if form.is_valid():
            add_item= form.save(commit=False)
            add_item.customer=top_up_cust_account
            add_item.save()
            myamount=request.POST.get('amount')
           
            mycard=AllifmaalCustomersModel.objects.get(id=customer.id)# returns TO objects
            mycard.balance= int(initial_balance)+int(myamount)
            mycard.save()
            return redirect('allifmaalapp:AllifmaaltopUpCustomerAccount',pk=mycustid)#just redirection page
    context={
        "form":form,  
        "customer":customer,
        "topups":topups,
        "cust_acc_total":cust_acc_total,
        "title":title,
       

    }
    return render(request, 'allifmaalapp/payment/allifcustomers-top-ups.html', context)#th

##########################3 INVOICES #######################333
def allifmaal_invoices(request):
    title="Allifmaal Invoices"
    invoices=AllifmaalInvoicesModel.objects.filter(posting_inv_status="waiting")
    last_invoices=AllifmaalInvoicesModel.objects.order_by('invoice_number')[:6]
    context={
        "invoices":invoices,
        "last_invoices":last_invoices,
        "title":title,
    }

    return render(request,'allifmaalapp/invoices/invoices.html',context)

def create_allifmaal_invoice(request):

    last_inv= AllifmaalInvoicesModel.objects.all().order_by('id').last()
    last_obj=AllifmaalInvoicesModel.objects.last()
    if last_obj:
        
        last_obj_id=last_obj.id
        last_obj_incremented=last_obj_id+1
   
    #purchaseNumber= 'LPO/AMEL-'+str(uuid4()).split('-')[1]
        purchaseNumber= 'AM/INV/'+'/'+str(last_obj_incremented)
        print(purchaseNumber)
    else:
       
        
        purchaseNumber= 'AM/INV/'+str(uuid4()).split('-')[1]
        #purchaseNumber= 'LPO/AMEL-'+str(uuid4()).split('-')[1]+'/'+str("Reset")

    newPurchaseOrder= AllifmaalInvoicesModel.objects.create(invoice_number=purchaseNumber)
    newPurchaseOrder.save()
    return redirect('allifmaalapp:allifmaal_invoices')

def delete_allifmaal_invoice(request,pk):
    AllifmaalInvoicesModel.objects.get(id=pk).delete()
    return redirect('allifmaalapp:allifmaal_invoices')

def add_allifmaal_invoice_details(request,pk):
    title="Invoice Details "
    inv_details=AllifmaalInvoicesModel.objects.filter(id=pk)
    try:
        my_inv_id=AllifmaalInvoicesModel.objects.get(id=pk)
        ourid=my_inv_id.id
        
    except:
        messages.error(request, 'Something went wrong and could not get the invoice')
        return redirect('allifmaalapp:allifmaal_invoices')

    service_Items = AllifmaalInvoiceItemsModel.objects.filter(allifinvitemconnector=my_inv_id)#this line helps to
    #show items that belong to that particular invoice in that particular invoice
    inv_id= get_object_or_404(AllifmaalInvoicesModel, id=pk)#this helps to fill that select field and invoice fields and content
    
    form=AddAllifmaalInvoiceDetailsForm(instance=my_inv_id)
   
    if request.method == 'POST':
        #add_shipment_items_form=AddShippmentItemsForm(request.POST)
        form=AddAllifmaalInvoiceDetailsForm(request.POST,request.FILES,instance=my_inv_id)
        if form.is_valid():
            form.save()
            print(request.POST)
            print("I have saved and itts correct")
            return redirect('allifmaalapp:add_allifmaal_invoice_items',pk=ourid)
    context={
        
        "form":form,
        "service_Items":service_Items,
       
        "my_inv_id":my_inv_id,
        "title":title,
        

    }
    return render(request,'allifmaalapp/invoices/invoice-details.html',context)
   


def add_allifmaal_invoice_items(request,pk):
    title="Add Invoice Items "
    global qaanshegto,myinvid
    try:
        qaanshegto =AllifmaalInvoicesModel.objects.get(id=pk)#very important to get id to go to particular shipment
        myinvid=qaanshegto.id
    except:
        return HttpResponse("Sorry there is a problem ! ")
   
    form=AddAllifmaalInvoiceItemsForm()
    add_inv= get_object_or_404(AllifmaalInvoicesModel, id=pk)
    initial_invoice_total=qaanshegto.invoice_total#this gives the initial invoice total
    if qaanshegto.customer:
        mycust=qaanshegto.customer#this gives the customer of the invoice
        customer_id=mycust.id#this gives the id of the customer specified in the invoice
        customer_account_balance=mycust.balance#this gets the account balance of the customer


    inv_Items = AllifmaalInvoiceItemsModel.objects.filter(allifinvitemconnector=qaanshegto)#this line helps to
    invoiceTotal = 0.0
    if len(inv_Items) > 0:
        for line in inv_Items:
            quantityTimesUnitPrice = float(line.quantity) * float(line.unit_price)
            invoiceTotal += quantityTimesUnitPrice
    
    myinvoice=AllifmaalInvoicesModel.objects.get(id=myinvid)
    myinvoice.invoice_total=int(invoiceTotal)
    myinvoice.save()

    add_item= None
    if request.method == 'POST':
        form=AddAllifmaalInvoiceItemsForm(request.POST)
        if form.is_valid():
            add_item= form.save(commit=False)
            add_item.allifinvitemconnector=add_inv
            add_item.save()
           # return HttpResponse(post)
            return redirect('allifmaalapp:add_allifmaal_invoice_items',pk=myinvid)#just redirection page

    context={
   
            "form":form,
            
            "qaanshegto":qaanshegto,
            "add_inv":add_inv,
            "invoiceTotal":invoiceTotal,
            "inv_Items":inv_Items,
            "title":title, 
    }
    return render(request,'allifmaalapp/invoices/add-invoice-items.html',context)

def delete_allifmaal_invoice_item(request,pk):
    AllifmaalInvoiceItemsModel.objects.get(id=pk).delete()
    #return redirect('logistics:add_invoice_items_alwen',pk=pk)#just redirection page
    return redirect('allifmaalapp:add_allifmaal_invoice_items',pk=myinvid)

def post_allifmaal_invoice(request,pk):
    global qaanshegto,myinvid
    try:
        qaanshegto =AllifmaalInvoicesModel.objects.get(id=pk)#very important to get id to go to particular shipment
        myinvid=qaanshegto.id
    except:
        return HttpResponse("Sorry there is a problem ! ")
   
    form=AddAllifmaalInvoiceItemsForm()
    add_inv= get_object_or_404(AllifmaalInvoicesModel, id=pk)

    initial_invoice_total=qaanshegto.invoice_total#this gives the initial invoice total
    if qaanshegto.customer:
        mycust=qaanshegto.customer#this gives the customer of the invoice
        customer_id=mycust.id#this gives the id of the customer specified in the invoice
        customer_account_balance=mycust.balance#this gets the account balance of the customer
    else:
        return redirect('logistics:add_invoice_items_alwen',pk=myinvid)
    


    inv_Items = AllifmaalInvoiceItemsModel.objects.filter(allifinvitemconnector=qaanshegto)#this line helps to
    invoiceTotal = 0.0
    if len(inv_Items) > 0:
        for line in inv_Items:
            quantityTimesUnitPrice = float(line.quantity) * float(line.unit_price)
            invoiceTotal += quantityTimesUnitPrice
    myinvoice=AllifmaalInvoicesModel.objects.get(id=myinvid)
    myinvoice.posting_inv_status="posted"
    myinvoice.save()
    #myinvoice.invoice_total=int(invoiceTotal)
    
    inv_tot=qaanshegto.invoice_total
    macaamil=AllifmaalCustomersModel.objects.get(id=customer_id)
    macaamil.balance=int(customer_account_balance)-int(inv_tot)
    
    macaamil.save()
    #client_detail, created = AllifPostedInvoicesModel.objects.get_or_create(customer=mycustomer,invoice_number=,invoice_total=)

    return redirect('allifmaalapp:post_allifmaal_invoice',pk=myinvid)
 
def allifpostedinvoices(request):
    title="Posted Invoices "
    #posted_invoices=AllifPostedInvoicesModel.objects.filter(posting_inv_status="posted")
    posted_invoices=AllifmaalInvoicesModel.objects.filter(posting_inv_status="posted")
    context={
        "posted_invoices":posted_invoices,

    }
    return render(request,'allifmaalapp/invoices/posted-invoices.html',context)
    
def allifmaal_invoice_to_pdf(request,pk):
    system_user=request.user
    invoice_details=get_object_or_404(AllifmaalInvoicesModel,id=pk)
    title="Invoice "+str(invoice_details)
    try:
        inv_number= AllifmaalInvoicesModel.objects.get(id=pk)
    except:
        messages.error(request, 'Something went wrong')

    invoiceItems = AllifmaalInvoiceItemsModel.objects.filter(allifinvitemconnector=inv_number)

    invoiceTotal = float(0.0)
    if len(invoiceItems) > 0:
       for x in invoiceItems:
            y = float(0 or x.quantity) * float(0 or x.unit_price)
            invoiceTotal += y

    template_path = 'allifmaalapp/invoices/allifmaal-inv-to-pdf.html'
    #companyDetails=AllifmaalDetailsModel.objects.all()
    #scope=AllifmaalScopeModel.objects.all()
    
    context = {
    'invoice_details':invoice_details,
   "invoiceItems":invoiceItems,
   #"companyDetails":companyDetails,
   "invoiceTotal":invoiceTotal,
   #"scope":scope,
   "system_user":system_user,
   "title":title,
   
    }
    
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="Allifmaal-invoice.pdf"'
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    try:
        pisa_status = pisa.CreatePDF(
       html, dest=response)
    except:
        return HttpResponse("Something went wrong!")
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    
    return response

########################################################## EXPENSES ############################################3
def allifmaalExpenses(request):
    title="Expenses"
    expenses=AllifmaalExpensesModel.objects.all()
    
   
    form=AddAllifmaalExpensesForm(request.POST or None)
    if request.method =="POST":
        form=AddAllifmaalExpensesForm(request.POST or None,request.FILES)
        if form.is_valid():
            form.save()
            form=AddAllifmaalExpensesForm()
    exp=0
    for expense in expenses:
        exp+=expense.amount
    total_exp=exp
    mycontext={
        
        "form":form,
        "expenses":expenses,
        "total_exp":total_exp,
        "title":title,
    }
    return render (request,'allifmaalapp/expenses/allifmaalexpenses.html',mycontext)

def deleteAllifmaalExpense(request,pk):
    AllifmaalExpensesModel.objects.get(id=pk).delete()
    return redirect('allifmaalapp:allifmaalExpenses')


################################## TASKS ###########################################


def allifmaal_Tasks(request):
    title="To do list"
   
    form =AddAllifmaalTasksForm(request.POST or None)
   
    #tasks=TasksModel.objects.order_by('complete','dueDate')
    tasks=AllifmaalTasksModel.objects.order_by('dueDate').filter(status="incomplete")
    completed_tasks=AllifmaalTasksModel.objects.filter(status="complete")
    

    if form.is_valid():
        form.save()
        messages.success(request, 'Task added successfully')
        form=AddAllifmaalTasksForm()#this clears out the form after adding the product

    context = {
        "form":form,
        "tasks":tasks,
        "title":title,
        "completed_tasks":completed_tasks,
        
        
    }

    return render(request,'allifmaalapp/tasks/allifmaaltasks.html',context)

def markAllifmaalTaskComplete(request,pk):
    mark_complete=AllifmaalTasksModel.objects.get(id=pk)
    if mark_complete.status=="incomplete":
        mark_complete.status="complete"
        mark_complete.save()
       
    else:
        mark_complete.status="incomplete"
        mark_complete.save()
      
    return redirect('allifmaalapp:allifmaal_Tasks')
def allifmaalCompletedTasksList(request):
    title="To do list"
   
    #tasks=TasksModel.objects.order_by('complete','dueDate')
    tasks=AllifmaalTasksModel.objects.filter(status="incomplete")
    completed_tasks=AllifmaalTasksModel.objects.filter(status="complete")

    context = {
        
        "tasks":tasks,
        "title":title,
        "completed_tasks":completed_tasks,
        
        
    }

    return render(request,'allifmaalapp/tasks/allifmaal-completed-tasks.html',context)


#@allowed_users(allowed_roles=['admin'])  
def delete_allifmaal_task(request,pk):
    try:
        AllifmaalTasksModel.objects.get(id=pk).delete()
    except:
        messages.error(request, 'Something went wrong')
        return redirect('todoapp:to-do-list ')

    return redirect('allifmaalapp:allifmaal_Tasks')


def update_allifmaal_tasks(request, pk):
    update_task= AllifmaalTasksModel.objects.get(id=pk)
    form = AddAllifmaalTasksForm(instance=  update_task)
   
    if request.method == 'POST':
        form = AddAllifmaalTasksForm(request.POST, instance=  update_task)
        if form.is_valid():
            form.save()
          
            return redirect('allifmaalapp:allifmaal_Tasks')
    context = {
		'form':form,
        " update_task": update_task,
    }
    return render(request, 'todoapp/toDoList.html', context)#this is the main page rendered first