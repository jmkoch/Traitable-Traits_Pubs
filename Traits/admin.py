from django.contrib import admin
from Pubs.models import Pub
from Traits.models import Trait
#from import_export import resources
from import_export.admin import ImportExportModelAdmin, ImportExportMixin, ImportMixin, ExportActionModelAdmin
from Traits.resources import TraitResource
from Traits.forms import TraitForm

# defining TraitInLine class (to have trait lines show up in Pub admin)
class TraitInline(admin.TabularInline):
	model = Trait
	show_change_link = True
	extra = 0  # this removes the blank data rows below; replaces them with 'add trait' option link.

# defining TraitAdmin class (useful & necessary for django-import-export module)
class TraitAdmin(ImportExportModelAdmin):
#class TraitAdmin(admin.ModelAdmin):
	autocomplete_fields = ['pub_reference'] #makes citekey an autocomplete field within Traits admin
	list_display = ('id', 'genus', 'species', 'isi', 'fruit_type', 'pub_reference')
	list_display_links = ('pub_reference', 'id')  # makes the citekey linkable on Trait admin interface
	resource_class = TraitResource
	form = TraitForm
	search_fields = ('genus', 'species', 'fruit_type') # adds search bar to Traits admin page; can add more fields to search thru
	#list_filter = ('fruit_type', 'genus', TraitListFilter) # adds filter bar to Traits admin page; nested filtering works too
	list_filter = ('genus', 'species', 'fruit_type')
	show_change_link = True


# registering our models - very important step!! if you forget to register a model, it won't show up on admin page.
admin.site.register(Trait, TraitAdmin)
#admin.site.register(TraitListFilter)
#admin.site.register(Person)