from django.urls import path

from . import views   # . means current directory
urlpatterns = [
    path("", views.index, name = "index"), 
    path("<str:name>", views.greet, name="greet"),
    path("youssef", views.youssef, name = "youssef" ),
    path("david", views.david, name = "david" )
    
]