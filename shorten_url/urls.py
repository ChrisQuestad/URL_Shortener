from django.urls import path
from . import views
from .views import *

app_name = 'shorten_url'
urlpatterns = [
    path('create', CreateURLView.as_view(), name='create'),
    path('detail/<str:pk>', views.detail, name='new_url'),
]
