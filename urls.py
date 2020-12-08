
from django.urls import path
from . import views

urlpatterns = [
    path('',views.final, name='final'),
    path('account/',views.account,name='account'),
    path('createt/',views.createt,name='createt'),

    path('login/',views.loginuser,name='login'),
    path('logout/',views.logoutuser,name='logout'),
    path('resource/',views.resource,name='resource')
]