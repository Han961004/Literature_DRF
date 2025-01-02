from django.urls import path
from .views.literature import *


urlpatterns = [
    path('v1/posts/', LiteratureView.as_view()),
    path('v1/posts/create/', LiteratureCreateView.as_view()),
    path('v1/posts/:id/', LiteratureDetailView.as_view()),
]
