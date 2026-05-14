from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from rest_framework.routers import DefaultRouter
from gor4eret.views import FootballClubViewSet

router = DefaultRouter()
router.register(r'football-clubs', FootballClubViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', RedirectView.as_view(url='/api/', permanent=False)),
]
