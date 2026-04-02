from rest_framework import serializers
from .models import Character, Empire, Ancestor

class CharacterSerializer(serializers.ModelSerializer):
    empire_name = serializers.CharField(source='empire.name', read_only=True)
    class Meta:
        model = Character
        fields = '__all__'
        
class EmpireSerializer(serializers.ModelSerializer):
    faction_display = serializers.CharField(source='get_faction_display', read_only=True)
    characters_count = serializers.IntegerField(source='character_set.count', read_only=True)
    class Meta:
        model = Empire
        fields = ['id', 'name', 'faction', 'faction_display', 'age', 
                  'territories', 'credo', 'anthem', 'description', 'image_url', 'ruler', 'heir']
        

class AncestorSerializer(serializers.ModelSerializer):
    parent_name = serializers.CharField(source='parent.name', read_only=True)
    children_count = serializers.IntegerField(source='children.count', read_only=True)
    
    class Meta:
        model = Ancestor
        fields = ['id', 'name', 'title', 'description', 'quote', 
                  'lifespan', 'image_url', 'parent', 'parent_name', 
                  'children_count', 'order']