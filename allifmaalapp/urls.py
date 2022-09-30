from django.urls import path
from . import views
app_name='allifmaalapp'
urlpatterns = [
path('', views.allifmaalmaindashboard, name="allifmaalmaindashboard"),
path('Allifmaal-Customers/', views.allifmaalcustomers, name="allifmaalcustomers"),
path('Allifmaal-Customer-Details/<int:pk>/', views.show_allifmaal_customer_details, name="show_allifmaal_customer_details"),
path('delete_customer/<str:pk>/', views.delete_allifmaal_customer, name="delete_allifmaal_customer"),
path('Update-Customer-Details/<str:pk>/', views.update_allifmaal_customer, name="update_allifmaal_customer"),

path('customer-top-up/<str:pk>/', views.AllifmaaltopUpCustomerAccount, name="AllifmaaltopUpCustomerAccount"),

############ invoices #################
path('Allifmaal-Invoices/', views.allifmaal_invoices, name="allifmaal_invoices"),
path('Create-New-Invoice/', views.create_allifmaal_invoice, name="create_allifmaal_invoice"),
path('Delete-This-Invoice!/<str:pk>/', views.delete_allifmaal_invoice, name="delete_allifmaal_invoice"),
path('Add-Invoice-Details/<str:pk>/', views.add_allifmaal_invoice_details, name="add_allifmaal_invoice_details"),
path('Add-Invoice-Items/<str:pk>/', views.add_allifmaal_invoice_items, name="add_allifmaal_invoice_items"),
path('Delete-Item-From-This-Invoice/<str:pk>/', views.delete_allifmaal_invoice_item, name="delete_allifmaal_invoice_item"),
path('Post-Invoice/<str:pk>/', views.post_allifmaal_invoice, name="post_allifmaal_invoice"),
path('Convert-Invoice-To-Pdf/<str:pk>/', views.allifmaal_invoice_to_pdf, name="allifmaal_invoice_to_pdf"),
path('Posted-Invoices/', views.allifpostedinvoices, name="allifpostedinvoices"),

##########################3333 expenses #####################
path('Allifmaal-Expenses/', views.allifmaalExpenses, name="allifmaalExpenses"),
path('Delete-Expense/<str:pk>/', views.deleteAllifmaalExpense, name="deleteAllifmaalExpense"),

####################### TASKS #################3
path('Allifmaal-Tasks/', views.allifmaal_Tasks, name="allifmaal_Tasks"),
path('Mark-This-Task-Complete/<str:pk>/', views.markAllifmaalTaskComplete, name="markAllifmaalTaskComplete"),
path('Completed-Tasks/', views.allifmaalCompletedTasksList, name="allifmaalCompletedTasksList"),
path('Delete-This-Task/<str:pk>/', views.delete_allifmaal_task, name="delete_allifmaal_task"),
path('Update-This-Task/<str:pk>/', views.update_allifmaal_tasks, name="update_allifmaal_tasks"),
      
]  
