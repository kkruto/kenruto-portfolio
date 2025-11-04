from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('tlw/', views.tlw_studio, name='tlw'),
    path('small-bets/', views.small_bets, name='small_bets'),
    path('kiota/', views.kiota, name='kiota'),
    path('gallery/', views.gallery, name='gallery'),
    path('newsletter/subscribe/', views.newsletter_subscribe, name='newsletter_subscribe'),
]