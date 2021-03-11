from django.urls import path
from .views import all_students_view, add_student ,student ,update_student ,delete_student ,user_login, logout_user, user_register, search


urlpatterns = [
    path("",all_students_view),
    path('search/',search),
    path('add',add_student),
    path('student/<str:id>',student),
    path('update/<str:id>',update_student,name='update'),
    path('delete/<str:id>',delete_student,name='delete'),
    path('login-user/',user_login),
    path('logout/',logout_user,name='logout'),
    path('register/',user_register,name="register")
]