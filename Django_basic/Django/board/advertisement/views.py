from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def advertisement_list(request, *args, **kwargs):
    return HttpResponse('<ul>'
                        '<li>Мастер по ремонту бытовой техники.</li>'
                        '<li>Ветеринар.</li>'
                        '<li>Уборка доома.</li>'
                        '<li>Сад и ландшафтный дизайн.</li>'
                        '<li>Строительныйе работы.</li>'
                        '</ul>')

def advertisement_upd(request, *args, **kwargs):
    return HttpResponse('<ul>'
                        '<li>Мастер по ремонту бытовой техники.</li>'
                        '<li>Ветеринар.</li>'
                        '<li>Уборка доома.</li>'
                        '<li>Сад и ландшафтный дизайн.</li>'
                        '<li>Сантехник.</li>'
                        '<li>Погрузочно-разгрузочные работы.</li>'
                        '<li>Строительныйе работы.</li>'
                        '</ul>')