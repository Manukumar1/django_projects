from django import forms

CLUSTER_TYPE = [
    (0, 'Simple Cluster'),
    (1, 'Detailed Cluster')
]

DAYSTOREAD_CLUSTER = [
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
]

DAYSTOREAD_UPDOWNGAP = [
    (1, '1'),
    (2, '2'),
    (3, '3')
]


class NextDayPredictionForm(forms.Form):
    choices_input = forms.BooleanField(
        label='Cluster with Gap: ',required=False,
        widget=forms.CheckboxInput)

    cluster_type_input = forms.CharField(
        label='Choose the type of cluster: ',
        widget=forms.Select(choices=CLUSTER_TYPE))

    clusterdays_input = forms.CharField(
        label='Choose the number of days for Cluster Reading: ', 
        widget=forms.Select(choices=DAYSTOREAD_CLUSTER))

    updowngap_input = forms.CharField(
        label='Choose the number of days for Up & Down Gap: ',
        widget=forms.Select(choices=DAYSTOREAD_UPDOWNGAP))

    def clean(self):
        cleaned_data = super(NextDayPredictionForm, self).clean()
        choices_input = cleaned_data.get('choices_input')
        cluster_type_input = cleaned_data.get('cluster_type_input')
        updowngap_input = cleaned_data.get('updowngap_input')
        clusterdays_input = cleaned_data.get('clusterdays_input')

        if not choices_input and not cluster_type_input and not updowngap_input and not clusterdays_input:
            raise forms.ValidationError('Please select the required options!')