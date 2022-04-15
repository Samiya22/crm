from django import forms

class LeadForm(forms.Form):
    ismi = forms.CharField(max_length=20)
    familyasi = forms.CharField(max_length=20)
    yoshi = forms.IntegerField(min_value=0)