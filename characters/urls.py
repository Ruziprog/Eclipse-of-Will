from django.urls import path
from .views import EclipseView, NoctisView, LumenView

urlpatterns = [
    path('', EclipseView.as_view(), name='eclipseofwill'),
    path('noctis/', NoctisView.as_view(), name='noctis'),
    path('lumen/', LumenView.as_view(), name='lumen'),
]