from django.urls import path
from .views import *

app_name = "mainsite"
urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("resources", ResourcesView.as_view(), name="resources"),
    path("contribute", ContributeView.as_view(), name="resources"),
    path("contact", ContactView.as_view(), name="contact"),
    path("classes", ClassesView.as_view(), name="classes"),
    path("thanks", ThanksView.as_view(), name="thanks"),
]
