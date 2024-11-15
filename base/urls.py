from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView,LogoutView
app_name='base'


urlpatterns=[
    path('login/',CustomLogInView.as_view(),name='login'),
    path('logout/',logout.as_view(),name='logout'),
    path('',TaskList.as_view(),name='tasks'),
    path('task/<int:pk>/',TaskDetail.as_view(),name='task'),
    path('create-task/',TaskCreate.as_view(),name='create-task'),
    path('update-task/<int:pk>/',TaskUpdate.as_view(),name='update-task'),
    path('delete-task/<int:pk>/',TaskDelete.as_view(),name='delete-task'),
]