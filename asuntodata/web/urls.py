from django.contrib import admin
from django.urls import path
from . import views

app_name = "web"

print("WEBURL")

urlpatterns = [
    path("pivot", views.dashboard_with_pivot, name="dashboard_with_pivot"),
    path("data", views.pivot_data, name="pivot_data"),
]
