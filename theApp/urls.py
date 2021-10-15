from django.urls import path

from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path("x/<str:slug>", views.redirectClient, name="redirect")
]
