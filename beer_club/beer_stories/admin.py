from django.contrib import admin

# Modeliu importas registras 
from .models import Types, Review

admin.site.register(Types)

# Dekoratorius ir admino klases apibrezimas
@admin.register(Review)
class BeerAdmin(admin.ModelAdmin):
    list_display = ('creator', 'name', 'beertype', 'rating', 'date')
    list_filter = ('creator', 'name', 'beertype', 'rating')