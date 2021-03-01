from django.urls import path
from .views import AllStudentsView,AddStudent


urlpatterns = [
    path("",AllStudentsView),
    path('add',AddStudent)
]