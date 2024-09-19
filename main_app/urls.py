from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('accounts/signup/', views.signup, name='signup'),
    path('my_players/', views.my_player_index, name='my_player_index'),
    path('players/', views.all_player_index, name='all_player_index'),
    path('players/<int:player_id>/', views.player_detail, name='player_detail'),
    path('players/create/', views.PlayerCreate.as_view(), name='player_create'),
    path('player/<int:pk>/update', views.PlayerUpdate.as_view(), name='player_update'),
    path('player/<int:pk>/delete', views.PlayerDelete.as_view(), name='player_delete'),
    path('players/<int:player_id>/add-job/', views.add_job, name='add_job'),
]
