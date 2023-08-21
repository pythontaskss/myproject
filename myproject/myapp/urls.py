from django.urls import path

from . import views

urlpatterns = [
    path('', views.base, name='base'),
    path('register/', views.register, name='register'),
    path('login_user', views.login_user, name='login_user'),
    path('logout_user', views.logout_user, name='logout_user'),
    path('add/', views.person_create_view, name='person_add'),
    path('<int:pk>/', views.person_update_view, name='person_change'),
    path('new/', views.new, name='new'),
    path('accept/', views.accept, name='accept'),
    path('ajax/load-branches/', views.load_branches, name='ajax_load_branches'), # AJAX
]

