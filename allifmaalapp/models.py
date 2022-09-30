from django.db import models

# Create your models here.
class AllifmaalCustomersModel(models.Model):
    Country = [
    ('Somalia', 'Somalia'),
     ('Somaliland', 'Somaliland'),
    ('Kenya', 'Kenya'),
     ('Other', 'Other'),
    ]
    name = models.CharField(null=True, blank=True, max_length=20)
    phone = models.CharField(null=True, blank=True, max_length=30)
    email= models.CharField(null=True, blank=True, max_length=100)
    country = models.CharField(choices=Country, blank=True, max_length=30)
    city= models.CharField(null=True, blank=True, max_length=30)
    address = models.CharField(null=True, blank=True, max_length=30)
    balance=models.DecimalField(max_digits=10,blank=True,null=True,decimal_places=2,default=0)
    contact = models.CharField(null=True, blank=True, max_length=30)

    def __str__(self):
        return '{}'.format(self.name)
class AllifmaalCustomerPaymentsModel(models.Model):
    
    customer= models.ForeignKey(AllifmaalCustomersModel,related_name="allifcustpaymentreltedname",on_delete=models.SET_NULL,blank=True,null=True)
    amount= models.DecimalField(max_digits=10,blank=True,null=True,decimal_places=2,default=0)
    date=models.DateField(auto_now=True)
    comments=models.CharField(max_length=15,blank=True,null=True, default='comment')
    
    def __str__(self):
        return '{}'.format(self.customer)

########################### INVOICES #################################
class AllifmaalInvoicesModel(models.Model):
    paymentTerms = [
    ('Cash', 'Cash'),
    ('Deposit', 'Deposit'),
    ('15 days', '15 days'),
    ('30 days', '30 days'),
   
    ]
    invoiceStatus = [
    ('Paid', 'Paid'),
    ('Current', 'Current'),
    ('Overdue', 'Overdue'),
   
    ]
    Currency = [
    ('KES','KES'),
    ('$', 'USD'),
    ('£', 'EURO'),
    ]
    posting_status = [
    ('waiting','waiting'),
    ('posted', 'posted'),
   
    ]
    #testingfield= models.ForeignKey(PurchaseOrdersModel,related_name="testingfieldrelatedname",on_delete=models.CASCADE,blank=True,null=True)
    customer= models.ForeignKey(AllifmaalCustomersModel,related_name="allifrelatcustinvoice",on_delete=models.SET_NULL,blank=True,null=True)
    invoice_number = models.CharField(null=True, blank=True, max_length=20)
    invoice_due_Date = models.DateField(null=True, blank=True)
    invoice_terms = models.CharField(choices=paymentTerms, default='Cash', max_length=20)
    invoice_status = models.CharField(choices=invoiceStatus, default='Current', max_length=20)
    invoice_currency = models.CharField(choices=Currency, default='$', max_length=20)
    invoice_comments=models.CharField(blank=True,null=True,default='invoice',max_length=20)
    date=models.DateField(blank=True,null=True,auto_now_add=True)
    invoice_total=models.DecimalField(max_digits=10,blank=True,null=True,decimal_places=2,default=0)
    posting_inv_status=models.CharField(choices=posting_status, default='waiting', max_length=100,blank=True,null=True)

    def __str__(self):
        return '{}'.format(self.invoice_number)

   
class AllifmaalInvoiceItemsModel(models.Model):
  
    description= models.CharField(max_length=30,blank=True,null=True)
    quantity = models.IntegerField(null=True, blank=True,default=0)
    unit_price = models.IntegerField(null=True, blank=True,default=0)
    allifinvitemconnector= models.ForeignKey(AllifmaalInvoicesModel, blank=True, null=True, on_delete=models.CASCADE,related_name='allifinvitemrelated')
    
    def __str__(self):
        return '{}'.format(self.description)
    #below calculates the total selling price for the model
    @property
    def selling_price(self):
        selling_price=self.quantity * self.unit_price
        return selling_price

class AllifmaalExpensesModel(models.Model):
  
    description=models.CharField(max_length=25,blank=True,null=True)
    amount=models.FloatField(max_length=20,blank=True,null=True,default=0)
    comments=models.CharField(max_length=20,blank=True,null=True)
    
    def __str__(self):
        return str(self.description)

class AllifmaalTasksModel(models.Model):
   
    task_status = [
    ('complete', 'complete'),
    ('incomplete', 'incomplete'),
    
    ]
    day = [
    ('Monday', 'Monday'),
    ('Tuesday', 'Tuesday'),
    ('Wednesday', 'Wednesday'),
    ('Thursday', 'Thursday'),
    ('Friday', 'Friday'),
    ('Saturday', 'Saturday'),
    ('Sunday', 'Sunday'),
    
    ]
    
    task = models.CharField(max_length=20,blank=False)
    status = models.CharField(max_length=10,choices=task_status,default='incomplete')
   
    createDate=models.DateTimeField(auto_now_add=True)
    dueDate=models.DateTimeField(auto_now_add=False,auto_now=False,blank=True,null=True)
    taskDay = models.CharField(max_length=10,choices=day,default='Monday')
    #assignedto=models.ForeignKey(AlwenDriversModel,on_delete=models.SET_NULL,blank=True,null=True,related_name="taskassignrelname")
    
    
    def __str__(self):
    		return self.task