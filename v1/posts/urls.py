from django.urls import path
from .views.literature import *


urlpatterns = [
    path('list/', LiteratureView.as_view()),
    path('create/', LiteratureCreateView.as_view()),
    path('detail/', LiteratureDetailView.as_view()),
]
