from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views_api import CharacterViewSet, EmpireViewSet

router = DefaultRouter()
router.register(r'characters', CharacterViewSet)
router.register(r'empires', EmpireViewSet)

urlpatterns = [
    path('', views.eclipseofwill, name='eclipseofwill'),
    path('noctis/', views.noctis, name='noctis'),
    path('lumen/', views.lumen, name='lumen'),
    path('freia/', views.freia, name='freia'),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]