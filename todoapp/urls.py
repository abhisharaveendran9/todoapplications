from django.urls import path
from todoapp import views

urlpatterns=[
    path("signup",views.SignUpView.as_view(),name="register"),
    path("login",views.LoginView.as_view(),name="signin")
]