from django.db import models
from django.conf import settings
from django.urls import reverse

# Create your models here.
USER = settings.AUTH_USER_MODEL


class ProfileModel(models.Model): #model for creating user profile 
    user = models.OneToOneField(USER, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=24)
    last_name = models.CharField(max_length=24)
    phone = models.TextField(max_length=12)
    location = models.TextField(max_length=30)
    photo = models.ImageField(upload_to="profile/image/", default="images/user.png")

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        url = reverse("user:profile_detail", kwargs={"pk": self.id})



  
    