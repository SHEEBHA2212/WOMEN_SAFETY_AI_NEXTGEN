from django.urls import path
from . import views

urlpatterns = [

    path("create/", views.create_complaint),
    path("list/", views.get_complaints),
    path("delete/<str:complaint_id>/", views.delete_complaint),
    path("track/<str:complaint_id>/", views.track_complaint),

]