from django.shortcuts import render
from dal import autocomplete
from Pubs.models import Pub

'''class CitekeyAutocomplete(autocomplete.Select2QuerySetView):
	def get_queryset(self):
		#if not self.request.is_authenticated():
		#	return Pub.objects.none()
		if self.request.user.is_authenticated:
			return Pub.objects.all()

		qs = Pub.objects.all()

		if self.q:
			qs = qs.filter(name__istartswith=self.q)

		return self.q
'''