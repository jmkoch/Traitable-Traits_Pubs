from dal import autocomplete
from django import forms
from Traits.models import Trait

class TraitForm(forms.ModelForm):
	class Meta:
		model = Trait
		fields = ('__all__')
		widgets = {
			'genus': autocomplete.ListSelect2(url='trait-autocomplete')
		}