from django.urls import path
from .views.login import LoginView
from .views.logout import LogoutView
from .views.user import *


urlpatterns = [
    path('v1/accounts/create/', UserView.as_view()),
    path('v1/accounts/login/', LoginView.as_view()),
    path('v1/accounts/logout11/', LogoutView.as_view()),
]
