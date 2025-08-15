from django.urls import path
from . import views
urlpatterns=[
    path('tribe/',views.tribe,name='tribe'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('home/',views.home,name='home'),
    path('',views.base,name=''),
    path('logout',views.logout,name='logout'),
    path('temp',views.temp,name='temp'),
    path('adddata',views.adddata,name='adddata'),
]