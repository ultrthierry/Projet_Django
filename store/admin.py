from django.contrib import admin
"""
permet d'indiquer à django les tables de la base de données qu'on souhaite administrer 
"""
# importer la table qu'on souhaite administrer
from .models import  Booking

# Register your models here.
admin.site.register(Booking)
