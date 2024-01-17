from django.urls import path
import users.views as views

urlpatterns = [
    path('', views.index_page, name='index'),
    path('login', views.login, name='login')
]