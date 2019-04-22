from django.contrib import admin
from Pubs.models import Pub
from Traits.models import Trait, Person
from import_export.admin import ImportExportModelAdmin
from Traits.resources import TraitResource

# defining TraitAdmin class (useful & necessary for django-import-export module)
class TraitAdmin(ImportExportModelAdmin):
	list_display = ('id', 'genus', 'species', 'isi', 'fruit_type', 'pub_reference')
	resource_class = TraitResource
	#list_filter = ()

class TraitInline(admin.TabularInline):
	model = Trait
	show_change_link = True

# registering our models - very important step!! if you forget to register a model, it won't show up on admin page.
admin.site.register(Trait, TraitAdmin)
admin.site.register(Person)
