from django.shortcuts import render, redirect
from .forms import NextDayPredictionForm
from django.http import HttpResponse
import requests
from .spreadsheet import NextDay


def predict(request):
    context1 = {}
    if request.method == 'POST':
        form = NextDayPredictionForm(request.POST)
        if form.is_valid():
            choices_input = form.cleaned_data.get('choices_input')
            cluster_type_input = form.cleaned_data.get('cluster_type_input')
            updowngap_input = form.cleaned_data.get('updowngap_input')
            clusterdays_input = form.cleaned_data.get('clusterdays_input')
            context1 = NextDay.calculateNextDay(daysToRead=clusterdays_input)

            return render(request, 'valueuno/about.html', {'context':context1})
    else:
        form = NextDayPredictionForm()
    return render(request, 'valueuno/nextDayPredictorForm.html', {'form': form})