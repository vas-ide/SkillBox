from django.shortcuts import render
# from django.http import HttpResponse
# Create your views here.


def advertisement_list(request, *args, **kwargs):
    return render(request, 'advertisement/advertisement_list.html', {})


def advertisement_upd(request, *args, **kwargs):
    return render(request, 'advertisement/advertisement_upd.html', {})


def veterinary_site(request, *args, **kwargs):
    return render(request, 'veterinary/veterinary_site.html', {})