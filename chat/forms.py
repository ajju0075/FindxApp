from django import forms
from chat.models import MessageModel


class MessageForm(forms.ModelForm):
    class Meta:
        model = MessageModel
        fields = ["message", "send_to", "host"]
