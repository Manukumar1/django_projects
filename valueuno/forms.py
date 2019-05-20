from django import forms

CHOICES = [
    ('cluster', 'Cluster-type'),
    ('updowngap', 'Up & Down Gap')
]

DAYSTOREAD_CLUSTER = [
    ('two', '2'),
    ('three', '3'),
    ('four', '4'),
    ('five', '5'),
]

CLUSTER_TYPE = [
    ('simple', 'Simple Cluster'),
    ('detailed', 'Detailed Cluster')
]

DAYSTOREAD_UPDOWNGAP = [
    ('one', '1'),
    ('two', '2'),
    ('three', '3')
]


class NextDayPredictionForm(forms.Form):
    choices_input = forms.MultipleChoiceField(
        label='Choose the options for predicting: ',
        widget=forms.CheckboxSelectMultiple, 
        choices=CHOICES) 

    cluster_type_input = forms.CharField(
        label='Choose the type of cluster for predicting: ', 
        widget=forms.Select(choices=CLUSTER_TYPE))

    updowngap_input = forms.CharField(
        label='Choose the number of days for Up & Down Gap: ', 
        widget=forms.Select(choices=DAYSTOREAD_UPDOWNGAP))

    clusterdays_input = forms.CharField(
        label='Choose the number of days for Cluster Reading: ', 
        widget=forms.Select(choices=DAYSTOREAD_CLUSTER))

    def clean(self):
        cleaned_data = super(NextDayPredictionForm, self).clean()
        choices_input = cleaned_data.get('choices_input')
        cluster_type_input = cleaned_data.get('cluster_type_input')
        updowngap_input = cleaned_data.get('updowngap_input')
        clusterdays_input = cleaned_data.get('clusterdays_input')

        if not choices_input and not cluster_type_input and not updowngap_input and not clusterdays_input:
            raise forms.ValidationError('Please select the required options!')