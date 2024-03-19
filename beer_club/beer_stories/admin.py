from django.contrib import admin
from django.utils.translation import gettext_lazy as _ 
from . import models



class ReviewsAdmin(admin.ModelAdmin):
    list_display = ['creator', 'name', 'beertype', 'rating', 'date', 'comments']
    list_filter = ['creator', 'name', 'beertype', 'rating']
    search_fields = ['name', 'rating']
    list_editable = ['rating', 'beertype']
    

class OriginAdmin(admin.ModelAdmin):
    list_display = ['name', 'types', 'color', 'filtered']
    list_filter = ['name', 'types', 'color', 'filtered']
    list_editable = ['types', 'color', 'filtered']
    search_fields = ['name']


admin.site.register(models.Review, ReviewsAdmin)
admin.site.register(models.Origin, OriginAdmin)