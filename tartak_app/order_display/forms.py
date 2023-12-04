from django import forms
from .models import Element, Order, Client
class ElementForm(forms.ModelForm):
    
    # name = forms.CharField(max_length=40, required=False)
    # width = forms.FloatField(required=False, min_value=0)
    # height = forms.FloatField(required=False, min_value=0)
    # length = forms.FloatField(required=False, min_value=0)
    # count = forms.IntegerField(required=False, min_value=0)
    # volume = forms.FloatField(required=False, min_value=0)
    # description = forms.Textarea()
    class Meta:
        model=Element
        fields = ['name', 'width', 'height', 'length', 'count', 'volume', 'description']
    
class OrderForm(forms.ModelForm):
    
    class Meta:
        
        model=Order
        fields = ['client','status','due']