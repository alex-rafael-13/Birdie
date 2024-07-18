from django.urls import path
from .views import get_birds, get_comments, get_user

urlpatterns = [
    path("/users", get_user, name="get_user"),
    path("/birds", get_birds, name="get_birds"),
    path("/comments", get_comments, name="get_comments")
]