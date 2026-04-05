from django.urls import path
from . import views

urlpatterns = [

    path("create/", views.create_complaint),
    path("list/", views.get_complaints),
    path("delete/<int:complaint_id>/", views.delete_complaint),

]