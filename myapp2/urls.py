from django.urls import path
from .views import AllStudentsView, AddStudent ,Student ,UpdateStudent ,DeleteStudent ,UserLogin, logoutUser, user_register, search


urlpatterns = [
    path("",AllStudentsView),
    path('search/',search),
    path('add',AddStudent),
    path('student/<str:id>',Student),
    path('update/<str:id>',UpdateStudent,name='update'),
    path('delete/<str:id>',DeleteStudent,name='delete'),
    path('login-user/',UserLogin),
    path('logout/',logoutUser,name='logout'),
    path('register/',user_register,name="register")
]