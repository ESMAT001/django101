from django.urls import path
from .views import AllStudentsView, AddStudent ,Student ,UpdateStudent ,DeleteStudent ,UserLogin


urlpatterns = [
    path("",AllStudentsView),
    path('add',AddStudent),
    path('student/<str:id>',Student),
    path('update/<str:id>',UpdateStudent),
    path('delete/<str:id>',DeleteStudent),
    path('login-user/',)
]