from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
path("", views.index, name="ShopHome"),
path('tracker/', views.tracker,name="TrackingStatus"),
path('contact/', views.contact,name="ContactUs"),
path('search/', views.search,name="Search"),
path('checkout/', views.checkout,name="Checkout"),
]