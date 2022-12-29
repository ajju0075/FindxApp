from django.urls import path
from chat import views as chat_views

app_name = "chat"
urlpatterns = [
    path("<int:pk>/", chat_views.ChatView.as_view(), name="chat"),
    path("list/", chat_views.ChatListView.as_view(), name="chat_list"),
    path(
        "user/<int:pk>/",
        chat_views.ChatCreateView.as_view(),
        name="chat_create",
    ),
    path(
        "user/<int:pk>/send/",
        chat_views.SendMessageView.as_view(),
        name="send_message",
    ),
]
