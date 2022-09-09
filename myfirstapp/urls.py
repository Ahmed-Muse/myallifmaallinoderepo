from django.urls import path
app_name='myfirstapp'
from . import views

urlpatterns = [
        #Leave as empty string for base url
	path('', views.myindexpage, name="myindexpage"),#this is the home page
	#path('about',views.about,name='about')
    
	#path('store/', views.store, name="store"),
	
]