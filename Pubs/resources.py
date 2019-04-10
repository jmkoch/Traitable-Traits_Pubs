from django.contrib import admin
from django.shortcuts import get_object_or_404
from Traits.models import Trait
from Pubs.models import Pub
from import_export.admin import ImportExportModelAdmin
from import_export import resources, fields, widgets
from import_export.fields import Field
from import_export.widgets import ForeignKeyWidget

# declaring Pub Resource below (resources are required & helpful for django-import-export module)
# when declaring a model's resource, follow this general setup:
# define class name with parameters (resources.ModelResource):
# then have a line with full_modelName = Field()
# then within the Meta class state the model, the fields to be printed, and the order in which they'll be printed
class PubResource(resources.ModelResource):

	class Meta:
		model = Pub
		clean_model_instances = True
		skip_unchanged = True  #optional variable that will skip unchanged data imports; DOESNT WORK!!!!
		report_skipped = True #optional variable that will not report skipped imports; DOESNT WORK!!! 
		fields = ['id', 'title', 'lastName', 'middleName', 'firstName', 'citekey', 'pub_type']
		export_order = ['id', 'title', 'lastName', 'middleName', 'firstName', 'citekey', 'pub_type']

	def dehydrate_full_pub(self, Pub):
		return '%s lastName %s firstName' % (Pub.lastName, Pub.firstName)

	# The before_import function will pass some tests prior to importing the data.
	def before_import(self, dataset, using_transactions, dry_run=True, collect_failed_rows=False, **kwargs):
		if 'id' not in dataset.headers:
			dataset.insert_col(0, lambda row: "", header='id')

		print('Here are the columns you will import: ')
		print(dataset.headers)

	# Here we will do a simple full_clean of our data before saving it to the database
	def before_save_instance(self, instance, using_transactions, dry_run):
		instance.full_clean()

	# function to export a csv containing all pub data entries
	def export_pubs_csv(request):
		response = HttpResponse(content_type='text/csv')
		response['Content-Disposition'] = 'attachmnet; filename = "pubs_output.csv"'

		writer = csv.writer(response)
		writer.writerow(['id', 'title', 'lastName', 'middleName', 'firstName', 'citekey', 'pub_type'])

		pubs = Pub.objects.all().values_list('id', 'title', 'lastName', 'middleName', 'firstName', 'citekey', 'pub_type')

		for pub in pubs:
			writer.writerow(pub)

		return response