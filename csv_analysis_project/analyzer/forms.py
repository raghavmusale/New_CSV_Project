from django import forms

class CSVUploadForms(forms.Form):
    file = forms.FileField(label="Upload a CSV File")