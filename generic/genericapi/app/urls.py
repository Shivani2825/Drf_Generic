
from django.urls import path
from .api import *

urlpatterns = [
    path("api/",StudentApi.as_view()),
    path("api/create/",StudentCreateApi.as_view()),
    path("api/update/<int:pk>",StudentUpdateApi.as_view()),
    path("api/delete/<int:pk>",StudentDeleteApi.as_view())
]
