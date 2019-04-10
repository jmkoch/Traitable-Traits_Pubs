from django.contrib import admin
from Pubs.models import Pub
from Traits.models import Trait
from import_export.admin import ImportExportModelAdmin
from Pubs.resources import PubResource

# defining PubAdmin class (useful & necessary for django-import-export module)
class PubAdmin(ImportExportModelAdmin):
	list_display = ('id', 'title', 'lastName', 'middleName', 'firstName', 'citekey', 'pub_type')
	form = PubForm
	resource_class = PubResource
	show_change_link = True
	inlines = [
		TraitInline,
	] # this inline adds Traits to Pub admin page to allow user to upload pub and trait in parallel

class PubInLine(admin.TabularInline):
	model = Pub

# registering our models - very important step!! if you forget to register a model, it won't show up on admin page.
admin.site.register(Pub, PubAdmin)