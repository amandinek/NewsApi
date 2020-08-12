
from django.urls import path
from .views import Home,Index, AlNews

urlpatterns = [
    path("",Home, name="Home"),
    path("bbc/",Index, name="Index"),
    path("aljasira/",AlNews,name="AlNews")

]