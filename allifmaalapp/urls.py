from django.urls import path
app_name='allifmaalapp'
from . import views

urlpatterns = [
        #Leave as empty string for base url
	path('allifmaaldashboard', views.allifmaalmaindashboard, name="allifmaalmaindashboard"),#this is the home page
	#path('about',views.about,name='about')
	
    
	#path('store/', views.store, name="store"),
	
]