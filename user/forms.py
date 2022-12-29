from django import forms
from user import models as user_models
from django.contrib.auth import forms as auth_forms
from django.contrib.auth import get_user_model

USER = get_user_model()

class Registrationform(auth_forms.UserCreationForm):
    class Meta:
        model = USER
        fields = ["username","email","password1","password2"]

class Loginform(auth_forms.AuthenticationForm):
    class Meta:
        model = USER
        fields = ["username","password"]

class ProfileForm(forms.ModelForm):
    class Meta:
        model = user_models.ProfileModel
        fields = ["first_name","last_name","phone","location","photo"]
        