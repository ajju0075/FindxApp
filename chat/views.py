from django.contrib.auth import get_user_model
from django.db.models import Count, F, Q
from django.shortcuts import render
from django.views import generic as views

from chat import forms as chat_forms
from chat import models as chat_models

USER = get_user_model()


class ChatView(views.DetailView):
    template_name = "chat/chat.html"
    model = chat_models.MessageModel
    context_object_name = "message"

    def get_queryset(self):
        qs = super().get_queryset()
        print(qs)
        return qs

    def get_object(self):
        pk = self.kwargs.get("pk")
        chat_object = self.get_queryset().get(send_to__id=pk)
        return chat_object

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        send_to = USER.objects.get(id=self.kwargs.get("pk"))
        host = self.request.user
        messages = chat_models.MessageModel.objects.filter(send_to=send_to, host=host)
        context["send_to"] = send_to
        context["messages"] = messages
        print("MESSAGES=====> ", messages)
        return context


class ChatListView(views.ListView):
    template_name = "chat/chat_list.html"
    model = chat_models.MessageModel
    context_object_name = "messages"


class ChatCreateView(views.CreateView):
    template_name = "chat/chat.html"
    model = chat_models.MessageModel
    form_class = chat_forms.MessageForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        send_to = USER.objects.get(id=self.kwargs.get("pk"))
        host = self.request.user
        messages = (
            chat_models.MessageModel.objects.filter(Q(host=host) | Q(send_to=host))
            # .filter(Q(send_to__message_host__host=send_to))
            .order_by("updated_on")
        )
        context["send_to"] = send_to
        context["messages"] = messages
        print("MESSAGES=====> ", messages)
        return context

    def get_success_url(self) -> str:
        url = self.request.META.get("HTTP_REFERER")
        return url

    def form_valid(self, form):
        # data = form.cleaned_data
        # message = data.get("message")
        # send_to = data.get("send_to")
        # message = chat_models.MessageModel.objects.create(
        #     message=message,
        #     send_to=send_to,
        #     host=self.request.user,
        # )
        form.instance.host = self.request.user
        return super().form_valid(form)

    def form_invalid(self, form):
        print("ERRORs====> ", form.errors, form)
        return super().form_invalid(form)


class SendMessageView(views.FormView):
    template_name = "chat/chat.html"
    form_class = chat_forms.MessageForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        send_to = USER.objects.get(id=self.kwargs.get("pk"))
        host = self.request.user
        messages = chat_models.MessageModel.objects.filter(send_to=send_to, host=host)
        context["send_to"] = send_to
        context["messages"] = messages
        print("MESSAGES=====> ", messages)
        return context

    def get_success_url(self) -> str:
        url = self.request.META.get("HTTP_REFERER")
        return url

    def form_valid(self, form):
        # data = form.cleaned_data
        # message = data.get("message")
        # send_to = data.get("send_to")
        # message = chat_models.MessageModel.objects.get_or_create(
        #     message=message,
        #     send_to=send_to,
        #     host=self.request.user,
        # )
        # form.instance.host = self.request.user
        # print("ERRORs====> ", form.errors)
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        print("ERRORs====> ", form.errors, form)
        return super().form_invalid(form)
