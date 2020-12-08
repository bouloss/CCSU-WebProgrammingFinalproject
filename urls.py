
from django.urls import path
from . import views

urlpatterns = [
    path('',views.final, name='final'),
    path('account/',views.account,name='account'),
    path('createt/',views.createt,name='createt'),
    #path('editt/<str:id>',views.editt,name='editt'),
    #path('deletet/<str:id>',views.deletet,name='deletet'),
]