from django.shortcuts import render
# from django.conf import settings
from django.views import View
from django.views.generic.base import TemplateView
# from django.http import HttpResponse
# from django.conf import settings as conf_settings
from data import *
import random


# class MyBaseView(TemplateView):


class MainView(TemplateView):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        data = {"title": title, "subtitle": subtitle, "description": description,
                "departures": departures, "tours": random.sample(list(tours.items()), 6)}  # tours
        return render(request, self.template_name, data)


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
