from django.shortcuts import render
from django.views import generic as views
from core import forms as core_forms
from django.contrib.auth import forms as auth_forms
from core import models as core_models
from django.urls import reverse_lazy
from django.conf import settings
from django.core.mail import send_mail  # for sending emails
from django.contrib import messages
from products import models as products_model



class HomeView(views.ListView):
    template_name = "core/home.html"
    model = products_model.ProductsModel
    context_object_name = "products"


class FeedbackCreateView(views.CreateView):
    template_name = "core/contactus.html"
    model = core_models.FeedbackModel
    form_class = core_forms.FeedbackForm
    success_url = reverse_lazy("core:home")

    def form_valid(self, form):
        data = form.cleaned_data
        name = data["name"]
        to_email = data["email"]
        subject = "Thank you for you feedback"
        message = f"""
        Hi {name},

        Thank you for your valuable feedback. We'll reach you soon as possible.


        FindX Team
        """
        from_email = settings.EMAIL_HOST_USER
        try:
            send_mail(
                subject=subject,
                message=message,
                from_email=from_email,
                recipient_list=[to_email],
            )
            messages.success(self.request, "Feedback send successfully!")
        except Exception:
            messages.error(self.request, "Something is went wrong! ")
        return super().form_valid(form)
