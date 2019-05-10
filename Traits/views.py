from django.shortcuts import render
from dal import autocomplete
from Traits.models import Trait

def welcome_page(request):
	return render(request, 'Traits/welcome_page.html', {})

class TraitAutocomplete(autocomplete.Select2QuerySetView):
	def get_queryset(self):
		if not self.request.is_authenticated():
			return Trait.objects.none()

		qs = Trait.objects.all()

		if self.q:
			qs = qs.filter(name__istartswith=self.q)

		return self.q
