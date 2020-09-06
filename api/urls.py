from django.urls import path
from api import views

urlpatterns = [
    path('', views.post_list.as_view(), name="post_list"),
    path('post_detail/<int:pk>', views.post_detail.as_view(), name="post_detail")
]
