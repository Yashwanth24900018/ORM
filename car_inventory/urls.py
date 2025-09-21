from django.contrib import admin
from django.urls import path
from inventory import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cars/', views.car_list, name="car_list"),  # URL for car list page
]
