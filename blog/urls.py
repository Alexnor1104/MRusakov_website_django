from django.urls import path
from blog import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blog', views.news_blog, name='blog'),
    path('single/', views.single, name='single'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),

]
