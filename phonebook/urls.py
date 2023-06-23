from django.contrib import admin
from django.urls import path
from phonebook_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.search, name='search'),
]
