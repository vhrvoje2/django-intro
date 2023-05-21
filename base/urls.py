from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.register_user, name="register"),
    path("login/", views.login_user, name="login"),
    path("logout/", views.logout_user, name="logout"),
    path("", views.home, name="home"),
    path("room/<str:pk>", views.room, name="room"),
    path("profile/<str:pk>", views.user_profile, name="user-profile"),
    path("create-room/", views.create_room, name="create-room"),
    path("edit-room/<str:pk>", views.edit_room, name="edit-room"),
    path("delete-room/<str:pk>", views.delete_room, name="delete-room"),
    path("delete-message/<str:pk>", views.delete_message, name="delete-message"),
    path("update-user/", views.update_user, name="update-user"),
    path("topics/", views.topics_page, name="topics"),
    path("activity/", views.activity_page, name="activity"),
]
