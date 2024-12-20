from django import forms

class DateForm(forms.Form):
    selected_date = forms.DateField(
        widget=forms.DateInput(attrs={
            'type': 'date',
            'style': (
                        'appearance: none;'
                        'padding: 0px;'
                        'border: none;'
                        'cursor: pointer;'
                        ),
        }),
        label="",
        required=False,
    )