from django.shortcuts import render
# from django.http import HttpResponse
# Create your views here.


def get_client_ip(request):
    ip = request.META.get('REMOTE_ADDR')
    return render(request, 'advertisement/advertisement_upd.html', {'ip_address': ip})


def advertisement_list(request, *args, **kwargs):
    return render(request, 'advertisement/advertisement_list.html', {})


def advertisement_upd(request, *args, **kwargs):
    return render(request, 'advertisement/advertisement_upd.html', {})


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