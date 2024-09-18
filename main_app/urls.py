from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('accounts/signup/', views.signup, name='signup'),
    path('my_players/', views.my_player_index, name='my_player_index'),
    path('players/', views.all_player_index, name='all_player_index'),
    path('players/<int:player_id>/', views.player_detail, name='player_detail')
]
