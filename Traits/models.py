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
    pub_reference = models.ForeignKey(Pub, blank=True, null=True, on_delete=models.PROTECT, verbose_name='citekey', validators=[val_alphanumeric])
    genus = models.CharField(max_length=50, null=True, blank=True, validators=[val_alpha])#help_text= 'Enter data if known. Expects str as input')
    species = models.CharField(max_length=50, null=True, blank=True, validators=[val_alpha])
    isi = models.FloatField(blank=True, null=True, validators=[MinValueValidator(0.0, message='Must be a number between 0.0 and 1.0'), MaxValueValidator(1.0, message='Must be a number between 0.0 and 1.0')], verbose_name='Index of Self-Incompatibility')
    
    FRUIT_TYPE_CHOICES = (('capsule','capsule'), ('CAPSULE', 'CAPSULE'), ('Capsule', 'Capsule'),('berry','berry'), ('Berry', 'Berry'), ('BERRY', 'BERRY')) # check why need doubles 
    fruit_type = models.CharField(max_length=50, null=True, blank=True, default='none', choices=FRUIT_TYPE_CHOICES)

    class Meta:
        verbose_name_plural = "Traits"

    def __str__(self):
        return (str(self.genus)+' '+str(self.species))