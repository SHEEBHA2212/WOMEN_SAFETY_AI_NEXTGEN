
from django.urls import path
from .views import submit_case
from .views import submit_case, get_cases

urlpatterns = [
    path('submit-case/', submit_case),
    path('get-cases/', get_cases),
]
