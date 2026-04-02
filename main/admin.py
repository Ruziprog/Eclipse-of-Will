from django.contrib import admin
from .models import Character, Empire, Ancestor

@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = ['name', 'empire', 'is_ruler', 'order']
    list_filter = ['empire', 'is_ruler']
    search_fields = ['name']
    actions = ['move_to_ancestors']
    
    def move_to_ancestors(self, request, queryset):
        """Переместить выбранных персонажей в Ancestors"""
        count = 0
        for character in queryset:
            # Создаём предка на основе персонажа
            Ancestor.objects.create(
                name=character.name,
                title=character.title if hasattr(character, 'title') else '',
                description=character.description,
                quote=character.quote,
                image_url=character.image_url,
                empire=character.empire,
                lifespan='',  # можно заполнить позже
                order=character.order
            )
            # Удаляем персонажа из Characters
            character.delete()
            count += 1
        
        self.message_user(request, f'{count} персонажей перемещено в Ancestors')
    move_to_ancestors.short_description = 'Переместить выбранных персонажей в Ancestors'

@admin.register(Empire)
class EmpireAdmin(admin.ModelAdmin):
    list_display = ('name', 'credo')
    search_fields = ('name', 'credo')

@admin.register(Ancestor)
class AncestorAdmin(admin.ModelAdmin):
    list_display = ['name', 'title', 'empire', 'lifespan', 'order']
    list_filter = ['empire']
    search_fields = ['name', 'title', 'description']
    list_editable = ['order']