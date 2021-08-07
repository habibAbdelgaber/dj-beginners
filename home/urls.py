from django.urls import path
from . import views

# from .views import home


urlpatterns = [
    path('', views.home, name='home-page'),
    path('create/', views.create, name='create'),
    path('detail/<str:pk>/', views.detail, name='post-detail'),
    path('detail/<str:pk>/update/', views.update, name='post-update'),
    path('detail/<int:pk>/delete/', views.delete, name='delete-post')
]