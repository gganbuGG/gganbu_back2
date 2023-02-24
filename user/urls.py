from django.urls import path,include
from .views import UserAPI,usersAPI,statAPI,stateAPI
from user import views
urlpatterns=[
    path('<str:sname>/', UserAPI.as_view()),
    path('info/<str:sname>/',usersAPI.as_view()),
    path('info/<str:sname>/stat',statAPI.as_view()),
    path('info/<str:sname>/state',stateAPI.as_view()),
    path('',views.info ),
    path('riot/riot.txt/', views.riot),
]