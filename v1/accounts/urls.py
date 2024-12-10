from django.urls import path
from .views.login import LoginView
from .views.logout import LogoutView
from .views.user import *


urlpatterns = [
    path('join/', UserView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
]
