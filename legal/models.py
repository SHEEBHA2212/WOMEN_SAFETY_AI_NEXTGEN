from django.db import models

class Case(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('taken', 'Taken'),
        ('resolved', 'Resolved'),
    ]

    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    issue = models.CharField(max_length=100)
    advocate = models.CharField(max_length=100)
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='pending'
    )

    def __str__(self):
        return f"{self.name} - {self.status}"