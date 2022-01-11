from .models import Product, Tag

from django.forms import ModelForm
from django import forms 

class ProductForm(ModelForm):

	class Meta:
		model = Product

		fields = ['prod_name','prod_description','prod_tags','prod_amount','prod_expires']

		widgets = {
		'prod_tags': forms.CheckboxSelectMultiple(),
		'prod_expires': forms.SelectDateWidget(),
		}

	def __init__(self, *args, **kwargs):

		super(ProductForm, self).__init__(*args, **kwargs)

		placeholder = iter(['Product Name','Product Description','','Total Amount',''])
		label = iter(['Name*',"Description","Tags","Total","Expires On: "])
		for name, field in self.fields.items():
			field.widget.attrs.update({'class': 'form-control','placeholder':next(placeholder)})
			self.fields[name].label = next(label)
		
class TagForm(ModelForm):

	class Meta:
		model = Tag

		fields = ['name']

		# fields[0].widget.attrs.update({'class':'form-control'})

	def __init__(self, *args, **kwargs):

		super(TagForm, self).__init__(*args, **kwargs)

		for name, field in self.fields.items():

			field.widget.attrs.update({'class': 'form-control','placeholder':'Tag Name'})
			self.fields[name].label="Name*"