from . import views
from django.urls import path
app_name= "mainview"

urlpatterns = [
    path('' , views.index,name="index" ),

]