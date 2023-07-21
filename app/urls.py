from django.urls import path
from app import views

urlpatterns = [
    path('', views.loginpage, name='login'),
    path('home/', views.home, name='home'),
    path('acttendence/', views.acttendence, name='actendentce'),
    path('event/', views.event, name= 'event'),
    path('registerevent/', views.registerevent, name='registerevent'),
    path('logout/', views.logoutpage, name='logout'),
    path('modifyevent/', views.modifyevent, name='modifyevent')
]