from django.db import models
from datetime import datetime

class Complaint(models.Model):

    ISSUE_CHOICES = [
        ('Harassment', 'Harassment'),
        ('Bullying', 'Bullying'),
        ('Unsafe Environment', 'Unsafe Environment'),
        ('Discrimination', 'Discrimination'),
        ('Other', 'Other')
    ]

    STATUS_CHOICES = [
        ('Submitted', 'Submitted'),
        ('In Progress', 'In Progress'),
        ('Resolved', 'Resolved')
    ]

    complaint_id = models.CharField(
        max_length=20,
        unique=True,        # ✅ IMPORTANT (must be unique)
        blank=True
    )

    issue_type = models.CharField(max_length=100, choices=ISSUE_CHOICES)
    location = models.CharField(max_length=255, blank=True)
    description = models.TextField()
    contact = models.CharField(max_length=100, blank=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Submitted"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):

        if not self.complaint_id:
            today = datetime.now()
            date_part = today.strftime("%y%m%d")  # e.g. 260407

            # Count today's complaints
            count = Complaint.objects.filter(
                created_at__date=today.date()
            ).count() + 1

            # Ensure uniqueness (VERY IMPORTANT)
            while True:
                new_id = f"{date_part}{count:03d}"  # 260407001

                if not Complaint.objects.filter(complaint_id=new_id).exists():
                    self.complaint_id = new_id
                    break

                count += 1  # try next number

        super().save(*args, **kwargs)

    def __str__(self):
        return self.complaint_id