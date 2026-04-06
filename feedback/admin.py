from django.contrib import admin
from .models import Feedback

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display  = ["name", "overall_experience", "recommend", "submitted_at"]
    list_filter   = ["recommend", "overall_experience"]
    ordering      = ["-submitted_at"]