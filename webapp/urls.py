from django.urls import path
from . import views 

urlpatterns = [
    path('', views.homePage, name="homePage"),
    path('about/', views.aboutPage, name="aboutPage"),
    path('profile/<int:pk>/', views.profilePage, name="profilePage"),
    path('genre/<int:pk>/', views.genrePage, name="genrePage"),
    path('create_author/', views.createAuthorPage, name="createAuthorPage"),
    path('update_author/<int:pk>/', views.updateAuthor, name="updateAuthor"),
    path('delete_author/<int:pk>/', views.deleteAuthor, name="deleteAuthor"),

]
