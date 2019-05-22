from django.contrib import admin
from Pubs.models import Pub
from Traits.models import Trait
from import_export.admin import ImportExportModelAdmin, ImportExportMixin, ImportMixin, ExportActionModelAdmin
#from Pubs.resources import PubResource 
##from Traits.admin import TraitInline
from Pubs.forms import CitekeyForm
from publications.models.publication import Publication  # import Publication model from publications/models/publication.py


# defining PubAdmin class (useful & necessary for django-import-export module)
class PubAdmin(ImportExportModelAdmin):
	##list_display = ('id', 'title', 'lastName', 'middleName', 'firstName', 'citekey', 'pub_type')
	list_display = ('id', 'title')
	##list_display_links = ('citekey', 'id')
	#resource_class = PubResource
	form = CitekeyForm
	##search_fields = ('citekey', 'title', 'lastName', 'firstName', 'pub_type')
	search_fields = ('citekey', 'authors', 'title')
	##list_filter = ('lastName', 'firstName', 'pub_type')
	
	show_change_link = True
	##inlines = [
	##	TraitInline,
	##] # this inline adds Traits to Pub admin page to allow user to upload pub and trait in parallel


# registering our models - very important step!! if you forget to register a model, it won't show up on admin page.
admin.site.register(Pub, PubAdmin)