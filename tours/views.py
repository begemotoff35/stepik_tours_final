from typing import Optional

from django.shortcuts import render
# from django.conf import settings
from django.views import View
from django.views.generic.base import TemplateView
# from django.http import HttpResponse
from django.http import Http404
from data import *
import random


class MyBaseView(TemplateView):
    @staticmethod
    def set_common_context_data(context, set_departures=True):
        context['title'] = title
        context['subtitle'] = subtitle
        context['description'] = description
        if set_departures:
            context['departures'] = departures

    @staticmethod
    def get_departure_name(departure):
        name: Optional[str]
        name = name_low = departures.get(departure)
        if name:
            assert isinstance(name, object)
            name_low = name[0].lower() + name[1:]
        return name, name_low


class MainView(TemplateView):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        # Каждый раз получаем случайные карточки:
        random_tours = random.sample(list(tours.items()), 6)
        # расширяем словарь для доп. отображения:
        for tour_id, tour in random_tours:
            tour['departure_name'] = departures[tour['departure']]
        # Передаем данные:
        data = {"title": title, "subtitle": subtitle, "description": description,
                "departures": departures, "tours": random_tours}
        return render(request, self.template_name, data)


class DepartureView(MyBaseView):
    template_name = "departure.html"

    def get_context_data(self, **kwargs):
        context = super(DepartureView, self).get_context_data(**kwargs)
        self.set_common_context_data(context)
        departure = context['departure']
        if departure not in departures:
            raise Http404

        tour_number = 0
        price_min = 99999999999999999
        price_max = 0
        nights_min = 9999999999
        nights_max = 0
        departure_tours = list()
        for tour_id, tour in tours.items():
            if tour['departure'] == departure:
                departure_tours.append([tour_id, tour])  # используем список как в MainView (т.к. возможен общий шаблон)
                tour_number += 1
                tour_price = tour['price']
                tour_nights = tour['nights']
                if tour_price < price_min:
                    price_min = tour_price
                if tour_price > price_max:
                    price_max = tour_price
                if tour_nights < nights_min:
                    nights_min = tour_nights
                if tour_nights > nights_max:
                    nights_max = tour_nights

        departure_info = f'Найдено {tour_number} туров ' \
                         f'по цене от {price_min} до {price_max} ₽ ' \
                         f'и от {nights_min} ночей до {nights_max} ночей'

        departure_name, departure_name_low = self.get_departure_name(departure)

        context['departure_name'] = departure_name
        context['departure_name_low'] = departure_name_low
        context['departure_info'] = departure_info
        context['tours'] = departure_tours

        return context


class TourView(MyBaseView):
    template_name = "tour.html"

    def get_context_data(self, **kwargs):
        context = super(TourView, self).get_context_data(**kwargs)
        self.set_common_context_data(context)
        tour_id = context['id']
        tour = tours.get(tour_id)
        if tour is None:
            raise Http404

        departure_name, departure_name_low = self.get_departure_name(tour['departure'])

        context['departure_name'] = departure_name
        context['departure_name_low'] = departure_name_low
        context['tour'] = tour
        context['tour_stars'] = '★' * int(tour['stars'])

        return context


class TestView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'test.html', {'name': 'Александр', 'place': 'Мурино'})
