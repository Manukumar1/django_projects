from django.shortcuts import render, redirect
from .forms import NextDayPredictionForm
from django.http import HttpResponse
import requests
from .script import NextDayPridictor


def predict(request):
    context = {}
    if request.method == 'POST':
        form = NextDayPredictionForm(request.POST)
        if form.is_valid():
            choices_input = form.cleaned_data.get('choices_input')
            cluster_type_input = form.cleaned_data.get('cluster_type_input')
            updowngap_input = form.cleaned_data.get('updowngap_input')
            clusterdays_input = form.cleaned_data.get('clusterdays_input')
            context = NextDayPridictor.fun(daysToRead=clusterdays_input)

            return render(request, 'valueuno/nextDayPredictorForm.html', {'context':context,'form': form})
    else:
        form = NextDayPredictionForm()
    return render(request, 'valueuno/nextDayPredictorForm.html', {'form': form})