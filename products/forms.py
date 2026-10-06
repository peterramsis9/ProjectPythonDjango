from django import forms
from .models import Product
class ProductForm(forms.ModelForm):
   class Meta:
       model = Product
       fields = ['name', 'description', 'price', 'image', 'category']
      
   def __init__(self, *args, **kwargs):
      category_queryset = kwargs.pop('category_queryset', None)
      super().__init__(*args, **kwargs) 
      
      if category_queryset is not None:
          self.fields['category'].queryset = category_queryset
      