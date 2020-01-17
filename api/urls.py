from django.urls import path

from api.views import login

app_name = 'api'
urlpatterns = [
    path('login/login_c', login.login_c, name='login_login_c'),
]