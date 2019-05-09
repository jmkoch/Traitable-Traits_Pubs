from django.contrib import admin
from Pubs.models import Pub
from Traits.models import Trait
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from Traits.resources import TraitResource
from Traits.forms import TraitForm

class TraitListFilter(admin.SimpleListFilter):
	title = 'genus'
	parameter_name = 'genus'
	related_filter_parameter = 'trait__id__exact'

	def lookups(self, request, model_admin):
		list_of_questions = []
		queryset = Trait.objects.order_by('id')

		if self.related_filter_parameter in request.GET:
			queryset = queryset.filter(id=request.GET[self.related_filter_parameter])

		#for genus in queryset:
		#	list_of_questions.append(
		#		(str(genus.id), genus.genus)
		#	)
		#return sorted(list_of_questions, key=lambda tp: tp[1])

	def queryset(self, request, queryset):
		if self.value():
			return queryset.filter(id = self.value())
		return queryset


class TraitInline(admin.TabularInline):
	model = Trait
	show_change_link = True
	extra = 0  # this 

# defining TraitAdmin class (useful & necessary for django-import-export module)
#class TraitAdmin(ImportExportModelAdmin):
class TraitAdmin(admin.ModelAdmin):
	list_display = ('id', 'genus', 'species', 'isi', 'fruit_type', 'pub_reference')
	list_display_links = ('pub_reference', 'id')
	resource_class = TraitResource
	form = TraitForm
	search_fields = ('genus', 'species', 'fruit_type')
	list_filter = ('fruit_type', 'genus', TraitListFilter) # play around here later
	show_change_link = True


# registering our models - very important step!! if you forget to register a model, it won't show up on admin page.
admin.site.register(Trait, TraitAdmin)
#admin.site.register(TraitListFilter)
#admin.site.register(Person)