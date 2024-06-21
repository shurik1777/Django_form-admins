import logging
from django.shortcuts import get_object_or_404, render
# from django.utils import timezone
# from datetime import timedelta
from .models import Client

logger = logging.getLogger(__name__)


def index_main(request):
    return render(request, 'forms/index.html')


def about_main(request):
    return render(request, 'forms/about.html')


def new_page(request):
    context = {
        "title": "Главная страница",
    }
    logger.info("Index page accessed")
    return render(request, "forms/pre.html", context)


def users(request):
    clients = Client.objects.all()
    context = {
        "title": "Список всех клиентов",
        "clients": clients,
    }
    return render(request, "forms/users.html", context)
