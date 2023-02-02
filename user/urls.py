from django.urls import path,include
from .views import UserAPI,usersAPI,statAPI
urlpatterns=[
    path('', UserAPI),
    path('info/<str:sname>/',usersAPI.as_view()),
    path('info/<str:sname>/stat',statAPI.as_view()),

]