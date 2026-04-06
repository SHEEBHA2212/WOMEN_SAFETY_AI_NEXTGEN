from django.db import models

class Case(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    issue = models.CharField(max_length=100)
    advocate = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name