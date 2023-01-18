from django.urls import path,include
from .views import UserAPI,ProfilesAPI,ProfileAPI,MatchesAPI
urlpatterns=[
    path('', UserAPI),
    path('profile/',ProfilesAPI.as_view()),
    path('profile/<str:s_name>/',ProfileAPI.as_view()),
    path('profile/matches/',MatchesAPI.as_view()),
]