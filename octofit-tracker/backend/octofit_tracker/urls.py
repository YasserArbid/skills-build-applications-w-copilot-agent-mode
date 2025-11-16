
import os
from django.urls import path, include
from rest_framework import routers
from .views import UserViewSet, TeamViewSet, ActivityViewSet, LeaderboardViewSet, WorkoutViewSet, api_root

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'teams', TeamViewSet)
router.register(r'activities', ActivityViewSet)
router.register(r'leaderboard', LeaderboardViewSet)
router.register(r'workouts', WorkoutViewSet)

# Get codespace name from environment variable
codespace_name = os.environ.get('CODESPACE_NAME', None)
codespace_api_url = None
if codespace_name:
    codespace_api_url = f"https://{codespace_name}-8000.app.github.dev/api/"

urlpatterns = [
    path('api/', include(router.urls)),
    path('', api_root, name='api_root'),
]
