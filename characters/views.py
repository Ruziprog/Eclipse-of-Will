# from django.shortcuts import render

# def eclipseofwill_view(request):
#     context = {}
#     return render(request, 'eclipseofwill.html', context)

# def noctis_view(request):
#     context = {}
#     return render(request, 'noctis.html', context)

# def lumen_view(request):
#     context = {}
#     return render(request, 'lumen.html', context)

from django.views.generic import TemplateView

class EclipseView(TemplateView):
    template_name = "characters/eclipseofwill.html"

class NoctisView(TemplateView):
    template_name = "characters/noctis.html"

class LumenView(TemplateView):
    template_name = "characters/lumen.html"