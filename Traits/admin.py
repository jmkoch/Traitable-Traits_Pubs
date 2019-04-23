from django.contrib import admin
from Pubs.models import Pub
from Traits.models import Trait, Person
from import_export.admin import ImportExportModelAdmin
from Traits.resources import TraitResource
from Traits.forms import TraitForm

# defining TraitAdmin class (useful & necessary for django-import-export module)
#class TraitAdmin(ImportExportModelAdmin):
class TraitAdmin(admin.ModelAdmin):
	list_display = ('id', 'genus', 'species', 'isi', 'fruit_type', 'pub_reference')
	list_display_links = ('pub_reference', 'id')
	resource_class = TraitResource
	form = TraitForm
	search_fields = ('genus', 'species', 'fruit_type')
	list_filter = ('fruit_type', 'genus') # play around here later

class TraitInline(admin.TabularInline):
	model = Trait
	show_change_link = True

# registering our models - very important step!! if you forget to register a model, it won't show up on admin page.
admin.site.register(Trait, TraitAdmin)
admin.site.register(Person)
