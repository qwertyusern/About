
from django.urls import path
from .views import *

urlpatterns = [
    path('', blog),
    path('maqola/<int:pk>', maqola),
    path('about/', about),
    path('intervyu/', inter),
]