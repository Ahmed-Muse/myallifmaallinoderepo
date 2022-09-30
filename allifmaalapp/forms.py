from django import forms
from .models import AllifmaalCustomersModel,AllifmaalInvoicesModel,AllifmaalInvoiceItemsModel,AllifmaalCustomerPaymentsModel,AllifmaalExpensesModel,AllifmaalTasksModel

############################# start of datepicker customization ##############################
class DatePickerInput(forms.DateInput):#use this class whereever you have a date and it will give you the calender
    input_type = 'date'#
class TimePickerInput(forms.TimeInput):#use this wherever you have time input
    input_type = 'time'
class DateTimePickerInput(forms.DateTimeInput):#use this wherever you have datetime input
    input_type = 'datetime'
    ################################# end of datepicker customization ################################
class AddAllifmaalCustomerForm(forms.ModelForm):
    class Meta:
        model = AllifmaalCustomersModel
        fields = ['name','phone','email','country', 'city','address','contact']
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':''}),

            'phone':forms.TextInput(attrs={'class':'form-control','placeholder':''}),
            'email':forms.TextInput(attrs={'class':'form-control','placeholder':''}),
            'city':forms.TextInput(attrs={'class':'form-control','placeholder':''}),
            'address':forms.TextInput(attrs={'class':'form-control','placeholder':''}),
            'contact':forms.TextInput(attrs={'class':'form-control','placeholder':''}),
            'country':forms.Select(attrs={'class':'form-control'}),
        
        }

class AddAllifmaalInvoiceDetailsForm(forms.ModelForm):
    class Meta:
        model = AllifmaalInvoicesModel
        fields = ['customer','invoice_terms', 'invoice_due_Date','invoice_status','invoice_currency','invoice_comments','posting_inv_status']

        widgets={
            'invoice_comments':forms.TextInput(attrs={'class':'form-control'}),
            
            'customer':forms.Select(attrs={'class':'form-control'}),
            'invoice_terms':forms.Select(attrs={'class':'form-control'}),
            'invoice_status':forms.Select(attrs={'class':'form-control'}),
            'invoice_currency':forms.Select(attrs={'class':'form-control'}),
           
            'posting_inv_status':forms.Select(attrs={'class':'form-control'}),

            #'invoice_due_Date':forms.DateInput(attrs={'class':'form-control'}),
            'invoice_due_Date' : DatePickerInput(attrs={'class':'form-control'}),
            
            #form-control here is the css class that we are passing
        }
        #fields='__all__'# this was used because of an error when running and the error said " .

class AddAllifmaalInvoiceItemsForm(forms.ModelForm):
    class Meta:
        model = AllifmaalInvoiceItemsModel
        fields = ['description','quantity','unit_price' ]

        widgets={
            'description':forms.TextInput(attrs={'class':'form-control'}),
            'quantity':forms.TextInput(attrs={'class':'form-control'}),
            'unit_price':forms.TextInput(attrs={'class':'form-control'}),
            
        }

class AddAllifmaalCustomerPaymentForm(forms.ModelForm):
    class Meta:
        model =AllifmaalCustomerPaymentsModel
        fields = ['customer','amount','comments']
        widgets={
            'amount':forms.TextInput(attrs={'class':'form-control','placeholder':''}),
            'comments':forms.TextInput(attrs={'class':'form-control','placeholder':''}),
            'customer':forms.Select(attrs={'class':'form-control'}),
        
        }

class AddAllifmaalExpensesForm(forms.ModelForm):
    class Meta:
        model = AllifmaalExpensesModel
        fields = ['description', 'amount','comments']
        widgets={
           
            'description':forms.TextInput(attrs={'class':'form-control'}),
            'amount':forms.TextInput(attrs={'class':'form-control'}),
            'comments':forms.TextInput(attrs={'class':'form-control'}),
           

            }

class AddAllifmaalTasksForm(forms.ModelForm): #the forms here is the one imported up there.
    class Meta:
        model = AllifmaalTasksModel
        fields = ['task','status','dueDate','taskDay']
        widgets={
            
            'task':forms.TextInput(attrs={'class':'form-control','placeholder':''}),
            
            'dueDate':DatePickerInput(attrs={'class':'form-control','placeholder':'Task due date'}),
            'taskDay':forms.Select(attrs={'class':'form-control'}),
            'status':forms.Select(attrs={'class':'form-control'}),
            
            
            
            #form-control here is the css class that we are passing
        } 