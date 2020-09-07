from django.urls import path
from api import views

urlpatterns = [
    path('', views.post_list.as_view(), name="post_list"),
    path('post_detail/<int:pk>', views.post_detail.as_view(), name="post_detail"),
    path('login/', views.login, name="login"),
    path('api/login', views.api_login.as_view(), name="api_login"),
    path('api/logout', views.api_logout.as_view, name="api_logout"),
]
