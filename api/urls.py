from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    path('games', views.GamesGet, name="get-all-games"),
    path('game/<int:pk>', views.GameGet, name="get-game-with-id"),
    path('cases', views.CasesGet, name="get-all-cases"),
    path('cases/<int:limit>', views.CasesGetLimit, name="get-limit-cases"),
    path('calculate-fps', views.CalculateFps, name="calculate-fps"),
]