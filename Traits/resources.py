from django.contrib import admin
from django.shortcuts import get_object_or_404
from Traits.models import Trait
from Pubs.models import Pub
from import_export.admin import ImportExportModelAdmin
from import_export import resources, fields, widgets
from import_export.fields import Field
from import_export.widgets import ForeignKeyWidget
from publications.models.publication import Publication 

# declaring Trait Resource below (resources are required & helpful for django-import-export module)
# when declaring a model's resource, follow this general setup:
# define class name with parameters (resources.ModelResource):
# then have a line with full_modelName = Field()
# then within the Meta class state the model, the fields to be printed, and the order in which they'll be printed
class TraitResource(resources.ModelResource):
    pub_reference = fields.Field(
    	column_name = 'pub_reference',
 	    attribute = 'pub_reference',
    	widget = ForeignKeyWidget(Publication, 'citekey') # changed here from Pub to Publication
    )

   # pub_reference = fields.Field(column_name = 'pub_reference', attribute = 'pub_reference', widget=widgets.ForeignKeyWidget(Pub, 'citekey'))

    class Meta:
        model = Trait
        clean_model_instances = True
        skip_unchanged = True
        report_skipped = True
        #exclude = ('id', )
        #import_id_fields = ('pub_reference')
        #fields = ('__all__')
        fields = ['id', 'genus', 'species', 'isi', 'fruit_type', 'pub_reference']
        export_order = ['id', 'genus', 'species', 'isi', 'fruit_type', 'pub_reference']

    def dehydrate_full_title(self, Trait):
        return '%s genus %s species' (Trait.genus, Trait.species)

	# before importing csv, this checks for a blank 'id' col. This adds 'id' col if not present
    def before_import(self, dataset, using_transactions, dry_run=True, collect_failed_rows=False, **kwargs): #raise_errors=True
        if 'id' not in dataset.headers:
            dataset.insert_col(0, lambda row: "", header='id')
        #fields = ('__all__')
        fields = ['id', 'genus', 'species', 'isi', 'fruit_type', 'pub_reference']

# need to fix this; doesn't break but doesn't work; still prints 'Here are the columns you'll import:' and includes bad column (but dosn't upload it)
        #for i in fields:
        #	if i not in fields:
        #		print('We found unrecognized/unexpected data in your csv. Skipping column: '+ str(col_name))
        print('Here are the columns you will import:' )
        print(dataset.headers)

    def before_save_instance(self, instance, using_transactions, dry_run):
        instance.full_clean()

    # function to export all trait entries into a csv
    def export_traits_csv(request):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="traits_output.csv"'

        writer = csv.writer(response)
        writer.writerow(['id', 'genus', 'species', 'isi', 'fruit type', 'pub_reference'])

        traits = Trait.objects.all().values_list('id', 'genus', 'species', 'isi', 'fruit_type', 'pub_reference')
	    
        for trait in traits:
            writer.writerow(trait)

        return response
        