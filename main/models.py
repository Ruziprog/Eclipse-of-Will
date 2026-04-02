from django.db import models

class Character(models.Model):
    class Gender(models.TextChoices):
        MALE = 'M', 'Male'
        FEMALE = 'F', 'Female'

    name = models.CharField("Name", max_length=100)
    age = models.IntegerField("Age")
    gender = models.CharField("Gender", max_length=10, choices=Gender.choices)
    ability = models.CharField("Ability", max_length=100)
    description = models.TextField("Description")
    image_url = models.URLField('URL images', max_length=500, blank=True, null=True)
    quote = models.CharField("Quote", max_length=200, blank=True, null=True)
    empire = models.ForeignKey(
        'Empire',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Принадлежность к Империи"
    )
    is_ruler = models.BooleanField("Is Ruler", default=False)
    has_will = models.BooleanField("Has Imperial Will", default=False)
    weight = models.IntegerField("Weight", blank=True, null=True)
    height = models.IntegerField("Height", blank=True, null=True)
    order = models.IntegerField(default=0, verbose_name="Порядок отображения")

    class Meta:
        verbose_name = 'Character'
        verbose_name_plural = 'Characters'

    def __str__(self):
        return self.name
    
class Empire(models.Model):
    class Faction(models.TextChoices):
        NOCTIS = 'NOCTIS', 'Noctis'
        LUMEN = 'LUMEN', 'Lumen'
        OTHER = 'OTHER', "Other"
    name = models.CharField("Name", max_length=100)
    credo = models.CharField("Credo", max_length=200)
    ruler = models.CharField("Rulers", max_length=50, blank=True, null=True)
    heir = models.CharField("Heir", max_length=100, blank=True, null=True)
    anthem = models.TextField("Anthem", blank=True, null=True)
    description = models.TextField("Description")
    image_url = models.URLField('URL images', max_length=500, blank=True, null=True)
    faction = models.CharField("Faction", max_length=20, choices=Faction.choices, default=Faction.OTHER)
    order = models.IntegerField(default=0, verbose_name="Порядок отображения")

    class Meta:
        verbose_name = 'Empire'
        verbose_name_plural = 'Empires'

    def __str__(self):
        return self.name
    
class Ancestor(models.Model):
    name = models.CharField("Name", max_length=100)
    title = models.CharField("Title", max_length=200, blank=True, null=True)
    image_url = models.URLField('Image URL', max_length=500, blank=True, null=True)
    description = models.TextField("Description", blank=True)
    quote = models.CharField("Quote", max_length=200, blank=True, null=True)
    lifespan = models.CharField("Lifespan", max_length=50, blank=True, null=True)  # "1035-1080"
    order = models.IntegerField(default=0, verbose_name="Display order")
    
    # Связь с империей
    empire = models.ForeignKey(
        'Empire',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Empire"
    )
    
    # Для древовидной структуры (связь с родителем)
    parent = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Parent",
        related_name='children'
    )
    
    class Meta:
        verbose_name = 'Ancestor'
        verbose_name_plural = 'Ancestors'
        ordering = ['order', 'lifespan']
    
    def __str__(self):
        return self.name