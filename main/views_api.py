from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from .models import Character, Empire
from .serializers import CharacterSerializer, EmpireSerializer

class CharacterViewSet(viewsets.ModelViewSet):
    queryset = Character.objects.all().select_related('empire').order_by('name')
    serializer_class = CharacterSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['gender', 'empire', 'is_ruler', 'has_will']
    search_fields =  ['name', 'ability', 'description', 'quote']
    ordering_fields = ['name', 'age', 'created_at']

class EmpireViewSet(viewsets.ModelViewSet):
    queryset = Empire.objects.all().prefetch_related('character_set').order_by('name')
    serializer_class = EmpireSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['faction']
    search_fields = ['name', 'credo', 'description']
    ordering_fields = ['name', 'age', 'territories']