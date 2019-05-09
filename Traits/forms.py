from dal import autocomplete
from django import forms
from Traits.models import Trait
#import autocomplete_light

class TraitForm(forms.ModelForm):
	class Meta:
		model = Trait
		fields = ('__all__')

		#widgets = {
		#	'genus': autocomplete.TagSelect2(url='trait-autocomplete')
			#'genus': autocomplete.TextWidget('GenusAutocomplete')
		#}