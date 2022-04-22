from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   path("productapi/",views.productlist.as_view()),
#    path("productapi/",views.productcreate.as_view()),
#    path("productapi/<int:pk>/",views.productretrive.as_view()),
#    path("productapi/<int:pk>/",views.productupdate.as_view()),
   path("productapi/<int:pk>/",views.productdelete.as_view()),
    
]
