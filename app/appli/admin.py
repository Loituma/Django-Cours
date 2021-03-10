from django.contrib import admin
from appli.models import Kube, Contact
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ('nom', 'mail', 'titre', 'date') #Liste des champs a afficher
    search_fields = ('nom', 'mail') #Recherche par ces champs
    date_hierarchy = 'date'
    list_filter = ('nom', )
    # ordering = ('date', ) #Force l order sur un champ

# admin.site.register(Kube)
admin.site.register(Contact, ContactAdmin)