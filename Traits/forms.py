from dal import autocomplete
from django import forms
from django.forms import TextInput
from Traits.models import Trait
#import autocomplete_light

class TraitForm(forms.ModelForm):
	class Meta:
		model = Trait
		fields = ('__all__')
		widgets = {
			'isi': TextInput(),  # this widget removes the up/down arrows from the Traits isi fields
		}

		#widgets = {
		#	'genus': autocomplete.TagSelect2(url='trait-autocomplete')
			#'genus': autocomplete.TextWidget('GenusAutocomplete')
		#}