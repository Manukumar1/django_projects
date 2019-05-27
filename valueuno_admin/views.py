from django.shortcuts import render
from .script import NextDayPridictor


def admin(request):
    return render(request, 'valueuno_admin/home.html',{'data': NextDayPridictor.fun(4)})
