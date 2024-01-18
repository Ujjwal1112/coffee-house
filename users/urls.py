from django.urls import path
import users.views as views

urlpatterns = [
    path('', views.index_page, name='index'),
    path('login', views.user_login, name='login'),
    path('logout', views.user_logout, name='logout')
]