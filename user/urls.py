from django.urls import path,include
from .views import UserAPI,usersAPI,userAPI
urlpatterns=[
    path('', UserAPI),
    path('info/',usersAPI.as_view()),
    path('info/<str:sname>/',userAPI.as_view()),
    
    
]