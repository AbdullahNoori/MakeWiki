from django.conf.urls import url
from accounts.views import home_view, signup_view
from django.urls import path

urlpatterns = [
    path('signup/', signup_view, name="signup")
]