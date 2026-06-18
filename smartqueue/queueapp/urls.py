from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),

    path('register/', views.register, name='register'),

    path('login/', views.user_login, name='login'),

    path('logout/', views.user_logout, name='logout'),

    path('join/<int:service_id>/', views.join_queue, name='join_queue'),

    path('token/', views.my_token, name='my_token'),

    path('dashboard/', views.dashboard, name='dashboard'),

    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    
    path('display/', views.display_board, name='display_board'),

]

