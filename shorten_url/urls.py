from django.urls import path
from .views import *

app_name = 'shorten_url'
urlpatterns = [
    path('create', CreateURLView.as_view(), name='create'),
    path('detail', DetailURLView.as_view(), name='detail'),
    path('detail/<str:pk>', NewURLView.as_view(), name='new_url'),
]
