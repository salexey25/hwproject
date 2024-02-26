import logging

from django.shortcuts import render
from django.http import HttpResponse
from random import randint
from django.template import loader


# Create your views here.

LOGGER = logging.getLogger(__name__)

def main(request):
    # Подключаем логирование
    LOGGER.info('Index page accessed')
    # Загружаем шаблон. Шаблоны хранятся в другой директории > templates (настраивается через settings;
    template = 'hw1app/main.html'
    # Формируем шаблон
    return render(request, template)


def about(request):
    LOGGER.info('Index page accessed')
    template = 'hw1app/about.html'
    return render(request, template)
