from django.db import models

class Complaint(models.Model):
    ISSUE_CHOICES = [
        ('Harassment', 'Harassment'),
        ('Bullying', 'Bullying'),
        ('Unsafe Environment', 'Unsafe Environment'),
        ('Discrimination', 'Discrimination'),
        ('Other', 'Other')
    ]

    issue_type = models.CharField(max_length=100, choices=ISSUE_CHOICES)
    location = models.CharField(max_length=255, blank=True)
    description = models.TextField()
    contact = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.issue_type