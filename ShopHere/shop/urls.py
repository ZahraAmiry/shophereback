from django.urls import path, include
from .views import Helloword


urlpatterns = [
    path('hi/', Helloword),
]