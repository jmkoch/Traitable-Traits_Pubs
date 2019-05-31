from django.shortcuts import render
from dal import autocomplete
from Traits.models import Trait

def welcome_page(request):
	return render(request, 'Traits/welcome_page.html', {})