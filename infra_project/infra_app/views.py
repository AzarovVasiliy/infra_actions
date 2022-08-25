from django.http import HttpResponse


def index(request):
    return HttpResponse('Вот и все!')


def second_page(request):
    return HttpResponse('А это вторая страница!')
