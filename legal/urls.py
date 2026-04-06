
from django.urls import path
from .views import submit_case

urlpatterns = [
    path('submit-case/', submit_case),
]
