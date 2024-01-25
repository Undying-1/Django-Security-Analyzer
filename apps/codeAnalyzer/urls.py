from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('enter/', views.enter, name='enter'),
    path('analyze/', views.analyzer, name='analyze'),
    path('report/', views.report, name='report'),
    path('pentest/', views.pentest, name='pentest'),
    path('pentest-attack/', views.pentest_attack, name='pentest-attack'),

]


