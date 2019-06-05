from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('home/', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('contributors/', views.contributors, name='contributors'),
    path('status/', views.status, name="check-status"),
    path('grievances/', views.grievances, name="all-grievances"),
    path('contributors/cards/medium.html', views.medium),
    path('submit/', views.submitGrievance, name='submit-grievance'),
    path('search/', views.search, name='Search'),
]