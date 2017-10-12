from django import forms

# Creating form for FarmHistory year wise search
class YearForm(forms.Form):
    year = forms.CharField(label = 'year', max_length=4)
