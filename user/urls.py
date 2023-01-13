from django.urls import path,include
from .views import UserAPI,ProfileAPI

urlpatterns=[
    path('', UserAPI),
    path('profile/',ProfileAPI.as_view()),

]