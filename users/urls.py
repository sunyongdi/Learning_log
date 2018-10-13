"""为应用程序users定义URL模式"""
# vfrom django.conf.urls import include, url
from django.urls import path, re_path
# from django.contrib.auth.views import login # 问题
from django.contrib.auth.views import LoginView
# from django.contrib.auth import login
from . import views


urlpatterns = [
	# 登陆界面
	# path('login/',  login, {'template_name':'users/login.html'}, name='login'),
	path('login/', LoginView.as_view(template_name='users/login.html'), name="login"),
	path('logout/', views.logout_view, name='logout'), 
	# 注册界面
	path('register/', views.register, name='register'),

]

app_name  = 'users'