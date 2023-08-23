from django.urls import path, include
from .views import *

app_name = "post"

urlpatterns = [

    path("", IndexView.as_view(), name="index"),
    path("add_post/", AddPost.as_view(), name="add_post"),
    path("detail/<int:pk>", PostDetail.as_view(), name="detail"),
    path("user_thumb_up/", user_thumb_up, name="user_thumb_up"),
    path("user_thumb_down/", user_thumb_down, name="user_thumb_down"),


]
