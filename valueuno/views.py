# from django.shortcuts import render
# from .models import ValueUnoForm
#
#
# def home(request):
#     context = {
#         'days': ValueUnoForm.objects.all()
#     }
#     return render(request, 'valueuno/home.html', context)
#
#
# def about(request):
#     return render(request, 'valueuno/about.html', {'title': 'About'})


from django.shortcuts import render
from .forms import NextDayPredictionForm
import requests


def predict(request):
    if request.method == 'POST':
        form = NextDayPredictionForm(request.POST)
        if form.is_valid():
        	form.save()
    else:
        form = NextDayPredictionForm()
    return render(request, 'valueuno/nextDayPredictorForm.html', {'form': form})