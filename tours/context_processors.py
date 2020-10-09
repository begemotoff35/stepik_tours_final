from tours.data import title, subtitle, description, departures


# для вывода главного меню на каждой странице
def common_data(request):
    return {
        "title": title,
        "subtitle": subtitle,
        "description": description,
        "departures": departures,
    }
