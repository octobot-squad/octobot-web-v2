from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='index'),
    path('team/', views.team, name='team'),
    path('services/', views.services, name='services'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('blog/', views.blogview, name='blog'),
    path('blog/<int:id>/<slug:slug>', views.blog_detail, name='blog_detail'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]
