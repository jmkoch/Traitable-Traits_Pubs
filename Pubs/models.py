from django.db import models
from django.conf import settings
from django.utils import timezone
import csv
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator

# some validator declarations that I use within the Pub & Trait models
val_alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Error: only alphanumeric characters are allowed.')
val_alpha = RegexValidator(r'^[a-zA-Z]*$', 'Error: only alphabetic characters are allowed.')
val_numeric = RegexValidator(r'^[0-9]*$', 'Error: only numeric characters are allowed.')
# add in hyphens to names

# Pub model below; all Pub-related variables declared within it
class Pub(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True, verbose_name='Publication name')
    lastName = models.CharField(max_length=50, null=True, blank=True, validators=[val_alpha], verbose_name = "Author's last name")
    middleName = models.CharField(max_length=50, null=True, blank=True, validators=[val_alpha], verbose_name = "Author's middle name")
    firstName = models.CharField(max_length=50, null=True, blank=True, validators=[val_alpha], verbose_name = "Author's first name")
    citekey = models.CharField(max_length=50, unique=True, null=True, validators=[val_alphanumeric])#, verbose_name='name') #null=True, blank=False
    
    # for variables with multiple options, must define said options on one line (in pairs, as below) and the variable on separate line
    PUB_TYPE_CHOICES = (('article', 'article'), ('book','book'))
    pub_type = models.CharField(max_length=50, null=True, blank=True, choices=PUB_TYPE_CHOICES)

    class Meta:
        #Gives the proper plural name for admin
        verbose_name_plural = "Pubs"

    def __unicode__(self):
        return self.citekey

    def __str__(self):
        return self.citekey