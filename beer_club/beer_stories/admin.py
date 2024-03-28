from django.contrib import admin
from django.utils.translation import gettext_lazy as _ 
from . import models



class ReviewsAdmin(admin.ModelAdmin):
    list_display = ['creator','country_name', 'color', 'filtered','name', 'beertype', 'rating', 'date', 'comments']
    list_filter = ['creator', 'name', 'beertype', 'rating']
    search_fields = ['name', 'rating', 'color']
    list_editable = ['rating', 'beertype']
    

class TypeAdmin(admin.ModelAdmin):
    list_display = ['types']
    list_filter = ['types']
    list_editable = []
    search_fields = ['types']


admin.site.register(models.Review, ReviewsAdmin)
admin.site.register(models.Type, TypeAdmin)