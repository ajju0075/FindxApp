from django.urls import path
from user import views as user_views

app_name = "user"
urlpatterns = [
    path("singup/", user_views.SingUpView.as_view(), name="singup"),
    path("login/", user_views.LoginView.as_view(), name="login"),
    path("logout/", user_views.LogoutView.as_view(), name="logout"),
    path("forgot-password/", user_views.ForgotView.as_view(), name="forgot"),
    # Profile
    path(
        "profile/create/", user_views.ProfileCreateView.as_view(), name="profile_create"
    ),
    path(
        "profile/<int:pk>/detail/",
        user_views.ProfileDetailView.as_view(),
        name="profile_detail",
    ),
    path(
        "profile/<int:pk>/update/",
        user_views.ProfileUpdateView.as_view(),
        name="profile_update",
    ),
    path(
        "profile/<int:pk>/delete/",
        user_views.ProfileDeleteView.as_view(),
        name="profile_delete",
    ),
]
