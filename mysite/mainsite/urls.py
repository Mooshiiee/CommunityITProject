from django.urls import path
from .views import *

app_name = "mainsite"
urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    #path("resources", RecourcesView.as_view(), name="resources"),
    #path("contribute", ContributeView.as_view(), name="resources"),
    #path("contact", ContactVirew,as_view(), name="contact"),
]
