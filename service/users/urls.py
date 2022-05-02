from django.urls import path
from .views import UserListAPIView

app_name = 'user_app'
urlpatterns = [
    path('',UserListAPIView.as_view())
]