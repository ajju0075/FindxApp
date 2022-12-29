from django.db import models
from django.conf import settings

USER = settings.AUTH_USER_MODEL


class MessageModel(models.Model): 
    message = models.CharField(max_length=500)
    send_to = models.ForeignKey(
        USER, on_delete=models.CASCADE, related_name="message_send_to"
    )
    host = models.ForeignKey(
        USER, on_delete=models.CASCADE, related_name="message_host"
    )
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.message}"
