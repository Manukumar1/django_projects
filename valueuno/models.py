from django.db import models
from django import forms

DAYS_TO_READ = [tuple([x, x]) for x in range(2, 6)]


class ValueUnoForm(forms.Form):
    daystoread = forms.IntegerField(label='Select Days', widget=forms.Select(choices=DAYS_TO_READ))

    def __str__(self):
        return self.daystoread
