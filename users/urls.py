from django.urls import path
import users.views as views

urlpatterns = [
    path('', views.index_page, name='index'),
    path('login', views.user_login, name='login'),
    path('logout', views.user_logout, name='logout'),
    path('register', views.user_register, name='register'),
    path('profile', views.user_profile, name='profile'),
    path('edit_profile', views.edit_profile, name="edit_profile")
]