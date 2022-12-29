from django import forms
from core import models as core_models



class FeedbackForm(forms.ModelForm):
    class Meta:
        model = core_models.FeedbackModel
        fields = ["name", "email", "subject", "message"]





        