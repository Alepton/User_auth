from django.urls import path
from .views import RegisterView, LoginVeiw, UserView, Logout


urlpatterns = [
    path('register', RegisterView.as_view()),
    path('login', LoginVeiw.as_view()),
    path('user', UserView.as_view()),
    path('logout', Logout.as_view()),
]

