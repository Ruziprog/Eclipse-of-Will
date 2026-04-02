from django.shortcuts import render
from django.db import OperationalError
from main.models import Character, Empire, Ancestor

def get_lang(request):
    """Вынести получение языка в отдельную функцию (DRY)"""
    return request.GET.get('lang', 'en')

def eclipseofwill(request):
    lang = get_lang(request)
    
    try:
        characters = Character.objects.all().order_by('order', 'name')  # порядок
        empires = Empire.objects.all().order_by('name')
    except OperationalError:
        characters = []
        empires = []

    context = {
        'lang': lang,
        'characters': characters,
        'empires': empires,
    }
    return render(request, 'main/eclipseofwill.html', context)

def noctis(request):
    lang = get_lang(request)
    
    try:
        noctis_empire = Empire.objects.filter(faction='NOCTIS').first()
        royal_family = Character.objects.filter(
            empire=noctis_empire, 
            is_ruler=True
        ).order_by('order', 'name')
        
        # Предки из отдельной модели
        ancestors = Ancestor.objects.filter(empire=noctis_empire).order_by('order', 'lifespan')
        
    except OperationalError:
        royal_family = []
        ancestors = []

    return render(request, 'main/noctis.html', {
        'lang': lang,
        'royal_family': royal_family,
        'ancestors': ancestors,
    })

def lumen(request):
    return render(request, 'main/lumen.html', {'lang': get_lang(request)})

def freia(request):
    return render(request, 'main/freia.html', {'lang': get_lang(request)})