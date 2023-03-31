from django.contrib.auth.views import LoginView, LogoutView
from . import views
from django.urls import path
app_name = 'accounts'
urlpatterns = [
    path('signup', views.SignUp.as_view(), name='signup'),
    path('login', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),

]