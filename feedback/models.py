from django.db import models

class Feedback(models.Model):
    # Step 1 — Feature Ratings (1–5)
    ease_of_use        = models.IntegerField(null=True, blank=True)
    emergency_response = models.IntegerField(null=True, blank=True)
    legal_assistance   = models.IntegerField(null=True, blank=True)
    complaint_filing   = models.IntegerField(null=True, blank=True)
    nearby_help        = models.IntegerField(null=True, blank=True)
    overall_design     = models.IntegerField(null=True, blank=True)

    # Step 2 — Overall Experience
    overall_experience = models.CharField(max_length=20, blank=True)  # amazing/good/okay/poor/bad
    recommend          = models.CharField(max_length=20, blank=True)  # Definitely/Maybe/Not really
    best_feature       = models.CharField(max_length=50, blank=True)  # emergency/legal/complaint/etc.

    # Step 3 — Suggestions
    improvement        = models.TextField(blank=True)
    comments           = models.TextField(blank=True)
    name               = models.CharField(max_length=100, blank=True)

    submitted_at       = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback by {self.name or 'Anonymous'} at {self.submitted_at.strftime('%Y-%m-%d %H:%M')}"