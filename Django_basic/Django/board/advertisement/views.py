from django.shortcuts import render
# from django.http import HttpResponse
# Create your views here.


def get_client_ip(request):
    ip = request.META.get('REMOTE_ADDR')
    return render(request, 'advertisement/advertisement_upd.html', {'ip_address': ip})


def advertisement_list(request, *args, **kwargs):
    advertisements = [
        "Мастер по ремонту бытовой техники.",
        "Ветеринар.",
        "Сантехник.",
        "Строительные работы",
        "Экскаватор",
        "Уборка дома",
        "Сад и ландшафтный дизайн",
        "Погрузочно-разгрузочные работы",
    ]
    return render(request, 'advertisement/advertisement_list.html', {'advertisements': advertisements})


def advertisement_upd(request, *args, **kwargs):
    advertisements = [
        "Мастер по ремонту бытовой техники.",
        "Ветеринар.",
        "Сантехник.",
        "Строительные работы",
        "Экскаватор",
    ]
    return render(request, 'advertisement/advertisement_upd.html', {'advertisements': advertisements})


def repair(request, *args, **kwargs):
    return render(request, 'advertisement/repair.html', {})


def veterinary(request, *args, **kwargs):
    return render(request, 'advertisement/veterinary.html', {})


def plumber(request, *args, **kwargs):
    return render(request, 'advertisement/plumber.html', {})


def construction(request, *args, **kwargs):
    return render(request, 'advertisement/construction.html', {})


def excavator(request, *args, **kwargs):
    return render(request, 'advertisement/excavator.html', {})


def contacts(request, *args, **kwargs):
    return render(request, 'contacts/contacts.html', {})


def about(request, *args, **kwargs):
    return render(request, 'about/about.html', {})


def categories(request, *args, **kwargs):
    categories = [
        "Cтроительство",
        "Ремонт",
        "Ветеринария",
        "Медицинская помощь",
        "Обслуживание дома",
        "Перевозки",
    ]
    return render(request, 'categories/categories.html', {'categories': categories})


def region(request, *args, **kwargs):
    region = [
        "Краснодарский край.",
        "Ростовская область",
    ]
    return render(request, 'region/region.html', {'region': region})