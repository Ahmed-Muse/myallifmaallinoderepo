from django.urls import path
from . import views
app_name='allifmaalapp'
urlpatterns = [
path('Dashboard-Allifmaal-Engineering-Ltd/', views.allifmaalmaindashboard, name="allifmaalmaindashboard"),

      
]  
