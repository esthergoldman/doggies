from django import forms
from bootstrap_datepicker_plus import DatePickerInput


class SearchForm(forms.Form):
    datetime = forms.DateTimeField(widget=DatePickerInput())

    