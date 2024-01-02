from django import forms
from .models import Element, Order, Client
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Field

class ElementForm(forms.ModelForm):
    element_form = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    amount = forms.FloatField(min_value=0)
    class Meta:
        model=Element
        fields = ['element_form','name', 'width', 'height', 'length', 'description','unit']
        widgets = {
            'unit': forms.RadioSelect(),
        }
    unit = forms.ChoiceField(choices=Element.Units),
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            "element_form",
            'name',
            Row(
                'unit',
                Field('amount', id="amount"),
                ),
            Row(
                Column('width', css_class='form-group col-md-4 mb-0'),
                Column('height', css_class='form-group col-md-4 mb-0'),
                Column('length', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Submit('submit', 'Zatwierdź')
        )
    
class OrderForm(forms.ModelForm):
    order_form = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    class Meta:
        model=Order
        fields = ['order_form','client','status','due','adres', 'workers']
        widgets = {
            'workers': forms.CheckboxSelectMultiple,
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'order_form',
            'adres',
            Field('workers',id="workers"),
            Row(
                Column('client', css_class='form-group col-md-4 mb-0'),
                Column('status', css_class='form-group col-md-4 mb-0'),
                Column('due', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Submit('submit', 'Zatwierdź', id="order_submit")
        )