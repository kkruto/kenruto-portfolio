# core/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # Main pages
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('resume/', views.resume, name='resume'),
    
    # Content pages
    path('essays/', views.kiota, name='kiota'),
    path('essays/<slug:slug>/', views.article_detail, name='article_detail'),
    path('projects/', views.small_bets, name='small_bets'),
    path('projects/<int:pk>/', views.project_detail, name='project_detail'),
    path('gallery/', views.gallery, name='gallery'),
    
    # Optional/Other pages
    path('tlw/', views.tlw_studio, name='tlw'),
    
    # Forms
    path('newsletter/subscribe/', views.newsletter_subscribe, name='newsletter_subscribe'),
]