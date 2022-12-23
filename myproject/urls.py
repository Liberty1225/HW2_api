from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/position/', views.position_list),
    path('api/employee/', views.emoloyee_list),
]

