from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("users/", views.users, name="users"),
    path("manAndVan/", views.manAndVan, name="manAndVan"),
    path("manAndVan/", views.manAndVan, name="manAndVan"),
    path("Coach/", views.Coach, name="Coach"),
    path("WasteManagement/", views.WasteManagement, name="WasteManagement"),
    path("Courier/", views.Courier, name="Courier"),
    path("document/", views.document, name="document"),
    path("addDoc/", views.addDoc, name="addDoc"),
    path("viewDoc/", views.viewDoc, name="viewDoc"),
    path("acceptCus/<str:name>/<str:pagename>/", views.acceptCus, name="acceptCus"),
]
