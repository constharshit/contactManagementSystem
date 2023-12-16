# contacts/urls.py
from django.urls import path
from .views import contactList, contactDetail, contactCreate, contactEdit, contactDelete

urlpatterns = [
    path('', contactList, name='contactList'),
    path('contact/<int:pk>/', contactDetail, name='contactDetail'),
    path('contact/new/', contactCreate, name='contactCreate'),
    path('contact/<int:pk>/edit/', contactEdit, name='contactEdit'),
    path('contact/<int:pk>/delete/', contactDelete, name='contactDelete'),
]
