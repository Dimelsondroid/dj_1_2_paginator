import csv

from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse

from pagination.settings import BUS_STATION_CSV


def index(request):
    return redirect(reverse('bus_stations'))


with open(BUS_STATION_CSV, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    stations = []
    for line in reader:
        stations.append(line)
    CONTENT = stations[1:]


def bus_stations(request):
    page_number = int(request.GET.get('page', 1))
    paginator = Paginator(CONTENT, 10)
    page_content = paginator.get_page(page_number)
    context = {
        # 'bus_stations': ...,
        'page': page_content,
    }
    return render(request, 'stations/index.html', context)
