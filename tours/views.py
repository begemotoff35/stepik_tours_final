from django.shortcuts import render
# from django.conf import settings
from django.views import View
from django.views.generic.base import TemplateView
# from django.http import HttpResponse
# from django.conf import settings as conf_settings


class MainView(TemplateView):
    template_name = "index.html"
    '''
    def get(self, request, *args, **kwargs):
        html = conf_settings.TEMPLATE_DIR
        return HttpResponse(html)
    '''


class DepartureView(TemplateView):
    template_name = "departure.html"
    '''
    def get(self, request, *args, **kwargs):
        html = 'Departure'
        return HttpResponse(html)
    '''


class TourView(TemplateView):
    template_name = "tour.html"
    '''
    def get(self, request, *args, **kwargs):
        html = 'Tour'
        return HttpResponse(html)
    '''


class TestView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'test.html', {'name': 'Александр', 'place': 'Мурино'})
