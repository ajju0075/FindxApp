import requests
from django.conf import settings
from django.contrib import auth, messages
from django.contrib.auth import forms as auth_forms
from django.contrib.auth import get_user_model
from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views

from products import models as products_models
from user import forms as user_forms
from user import models as user_models

USER = get_user_model

# Create your views here.


class SingUpView(views.CreateView):
    template_name = "user/registration/registration.html"
    form_class = user_forms.Registrationform
    success_url = reverse_lazy("user:login")

    def form_valid(self, form):
        re_response = self.request.POST.get("g-recaptcha-response", None)
        url = settings.GOOGLE_RECAPTCHA_VERIFY_URL

        response = requests.post(
            url=url,
            data={
                "secret": settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                "response": re_response,
            },
        ).json()

        if response.get("success", None) is True:
            messages.success(self.request, "successfully created account login to continue")
            return super().form_valid(form)
        messages.error(self.request, "reCaptcha verification failed! Please try again.")
        return self.form_invalid(form)




class LoginView(auth_views.LoginView):
    template_name = "user/registration/login.html"
    form_class = user_forms.Loginform

    def form_valid(self, form):
        re_response = self.request.POST.get("g-recaptcha-response", None)
        url = settings.GOOGLE_RECAPTCHA_VERIFY_URL

        response = requests.post(
            url=url,
            data={
                "secret": settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                "response": re_response,
            },
        ).json()

        if response.get("success", None) is True:
            messages.success(self.request, "Logged in successfully as")
            return super().form_valid(form)
        messages.error(self.request, "recaptcha verification failed! Please try again.")
        return self.form_invalid(form)





class LogoutView(auth_views.LogoutView):
    template_name = "user/registration/logout.html"
    success_url = reverse_lazy("user:singup")

    def get_default_redirect_url(self):
        response = super().get_default_redirect_url()
        messages.success(self.request, "Logged out successfully!")
        return response


class ForgotView(views.TemplateView):
    template_name = "user/registration/forget.html"


# profile views


class ProfileCreateView(LoginRequiredMixin, views.CreateView):  # profile create
    form_class = user_forms.ProfileForm
    model = user_models.ProfileModel
    template_name = "user/user_profile/profile_create.html"
    success_url = reverse_lazy("core:home")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ProfileUpdateView(
    PermissionRequiredMixin, LoginRequiredMixin, views.UpdateView
):  # profile update
    form_class = user_forms.ProfileForm
    model = user_models.ProfileModel
    template_name = "user/user_profile/profile_update.html"
    success_url = reverse_lazy("core:home")

    def has_permission(self):
        user = self.request.user
        can_update_profile = False
        profile = user_models.ProfileModel.objects.get(id=self.kwargs.get("pk"))
        if profile.user == user:
            can_update_profile = True
        return can_update_profile

    # def get_success_url(self):
    #     url = reverse_lazy("user:profile_detail", kwargs={"pk": self.kwargs.get("pk")})
    #     return url


class ProfileDetailView(LoginRequiredMixin, views.DetailView):  # profile detail
    template_name = "user/user_profile/profile_detail.html"
    model = user_models.ProfileModel
    context_object_name = "profile"


class ProfileDeleteView(LoginRequiredMixin, views.DeleteView):  # profile delete
    template_name = "user/user_profile/profile_delete.html"


# profile views end here


