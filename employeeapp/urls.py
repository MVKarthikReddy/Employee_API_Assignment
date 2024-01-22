from django.urls import path, include
from employeeapp.views import UserRegistrationView,UserLoginView,UserProfileView


urlpatterns = [
       path("register/", UserRegistrationView.as_view(), name="register-user"),
       path("login/", UserLoginView.as_view(), name="login-user"),
       path("profile/", UserProfileView.as_view(), name="profile"),
       
]