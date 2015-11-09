from django import forms
from Data.models import data

class BlogForm(forms.ModelForm):
	
	class Meta:
		model = data
		fields = '__all__'

	def getData(Meta):
			return Meta.data