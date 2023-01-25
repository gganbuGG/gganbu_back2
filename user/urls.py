from django.urls import path,include
from .views import UserAPI,userAPI
urlpatterns=[
    path('', UserAPI),
    path('info',userAPI.as_view()),
    
    
]