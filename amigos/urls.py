from django.urls import path
from .views import register_user, user_login, user_logout

urlpatterns = [
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('register/', register_user, name='register'),
]
