from django import forms

class ElementForm(forms.Form):
    name = forms.CharField(max_length=40, required=False)
    width = forms.FloatField(required=False, min_value=0)
    height = forms.FloatField(required=False, min_value=0)
    length = forms.FloatField(required=False, min_value=0)
    count = forms.IntegerField(required=False, min_value=0)
    volume = forms.FloatField(required=False, min_value=0)
    description = forms.Textarea()
    
class OrderForm(forms.Form):
    date_due = forms.DateField(required=False)