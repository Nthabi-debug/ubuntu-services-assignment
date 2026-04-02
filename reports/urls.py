from django.urls import path
from . import views

urlpatterns = [
    path('report/', views.report_issue, name='report_issue'),
    path('track/', views.report_list, name='report_list'),
    path('', views.report_list, name='home'),
]