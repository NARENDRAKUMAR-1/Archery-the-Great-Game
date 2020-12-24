from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('compute_scores', views.compute_scores,name='compute_scores')
]