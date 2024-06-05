from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home-page"),
    path('song/<str:pk>', views.song, name="song-page"),
    path('add-song/', views.addSong, name="add-song"),
    path('edit-song/<str:pk>', views.editSong, name="edit-song"),
    path('delete-song/<str:pk>', views.deleteSong, name="delete-song"),
    path('add-album/', views.addAlbum, name="add-album"),
    path('login/', views.loginPage, name="login"),
    path('register/', views.logoutPage, name="logout"),
]