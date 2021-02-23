from django import forms
from .models import items


class itemsForm(forms.ModelForm):
    class Meta:
        model=items
        fields=['item_name',"item_desc",'item_price','item_image']