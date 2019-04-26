from dal import autocomplete
from django import forms
from Pubs.models import Pub
#import autocomplete_light

class CitekeyForm(forms.ModelForm):
	class Meta:
		model = Pub
		fields = ('__all__')
		widgets = {
			'citekey': autocomplete.TagSelect2(url='citekey-autocomplete')
		}