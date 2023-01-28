from django.urls import path,include
from .views import UserAPI,usersAPI
urlpatterns=[
    path('', UserAPI),
    path('info/<str:sname>/',usersAPI.as_view()),

]