from django.db import models
from django.conf import settings
from django.utils import timezone
import csv
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator
from Pubs.models import Pub

# some validator declarations that I use within the Pub & Trait models
val_alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Error: only alphanumeric characters are allowed.')
val_alpha = RegexValidator(r'^[a-zA-Z]*$', 'Error: only alphabetic characters are allowed.')
val_numeric = RegexValidator(r'^[0-9]*$', 'Error: only numeric characters are allowed.')
# add in hyphens to names

# Trait model below; all Trait-related variables declared within it
class Trait(models.Model):
   # author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    pub_reference = models.ForeignKey(Pub, blank=True, null=True, on_delete=models.PROTECT, verbose_name='citekey', validators=[val_alphanumeric])#, related_name='name')
    genus = models.CharField(max_length=50, null=True, blank=True, validators=[val_alpha])#help_text= 'Enter data if known. Expects str as input')
    species = models.CharField(max_length=50, null=True, blank=True, validators=[val_alpha])
    isi = models.FloatField(blank=True, null=True, validators=[MinValueValidator(0.0, message='Must be a number between 0.0 and 1.0'), MaxValueValidator(1.0, message='Must be a number between 0.0 and 1.0')], verbose_name='Index of Self-Incompatibility')
    
    FRUIT_TYPE_CHOICES = (('capsule','capsule'), ('berry','berry')) # ('CAPSULE', 'CAPSULE'), ('Capsule', 'Capsule'),('berry','berry'), ('Berry', 'Berry'), ('BERRY', 'BERRY')) # check why need doubles 
    fruit_type = models.CharField(max_length=50, null=True, blank=True, default='none', choices=FRUIT_TYPE_CHOICES)

    class Meta:
        verbose_name_plural = "Traits"

    def __str__(self):
        return (str(self.genus)+' '+str(self.species))

    def __unicode__(self):
        return self.name

class RestrictedManager(models.Manager):
    ''' This manager filters out deleted sets'''
    def get_queryset(self):
        results = super(RestrictedManager, self).get_queryset().filter(safe_deleted=False)
        return results.filter(safe_deleted=False)
    def all_with_deleted(self):
        return super(RestrictedManager, self).get_queryset()
    def deleted_set(self):
        return super(RestrictedManager, self).get_queryset().filter(safe_deleted=True)

'''
class Person(models.Model):
    first_names = models.CharField(max_length=100, null=True, blank=True)
    middle_names = models.CharField(max_length=100, null=True, blank=True)
    last_names = models.CharField(max_length=100, null=True, blank=True)

    #flag kept for safe deletion
    safe_deleted=models.BooleanField(null=False,default=False)

    objects = models.Manager()
    rmobjects = RestrictedManager()

    def __unicode__(self):
        name = ''
        if self.first_names!=None:
            name += str(self.first_names)
        if self.middle_names!=None:
            name += " "+str(self.middle_names)
        if self.last_names !=None:
            name += " "+ str(self.last_names)
        return name


    def __str__(self):
        name = ''
        if self.first_names!=None:
            name += str(self.first_names)
        if self.middle_names!=None:
            name += " "+str(self.middle_names)
        if self.last_names !=None:
            name += " "+ str(self.last_names)
        return name
'''