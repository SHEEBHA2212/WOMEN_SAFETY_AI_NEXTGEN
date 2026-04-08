from django.db import models

class ChatMessage(models.Model):

    user_message = models.TextField()
    bot_reply = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_message

class ContactTicket(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=150)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"[{self.subject}] from {self.email}"