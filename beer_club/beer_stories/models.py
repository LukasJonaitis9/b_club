from django.contrib.auth import get_user_model
from django.db import models 
from django.urls import reverse
from django.utils.translation import gettext as _

<<<<<<< Updated upstream
class Origin(models.Model):
    name = models.CharField(max_length=200, help_text='Enter name of a beer type')

=======
class Type(models.Model):
>>>>>>> Stashed changes
    MAIN_TYPES = (
        ('Wheat beer', 'Wheat beer'),
        ('Pilsner', 'Pilsner'),
        ('IPA', 'IPA'),
        ('ALE', 'ALE'),
        ('Stout', 'Stout'),
        ('Bock', 'Bock'),
        ('Lager', 'Lager'),
    )
    types = models.CharField(max_length=10, choices=MAIN_TYPES, null=True, blank=True, help_text='Chose your type of beer!')
    country_name = models.CharField(max_length=200, help_text='Enter name of a beer type')
    COLOR_TYPES = (
        ('l', 'Light / Straw'),
        ('a', 'Amber'),
        ('c', 'Copper / Reddish-Brown'),
        ('b', 'Brown'),
        ('d', 'Black'),
    )

    color = models.CharField(max_length=1, choices=COLOR_TYPES, help_text='Choose your colour of beer!')

    FILTERED = (
        ('y', 'Filtered'),
        ('n', 'Unfiltered')
    )

    filtered = models.CharField(max_length=1, choices=FILTERED, null=True, blank=True, help_text='Choose filtered or unfiltered beer!')

    def __str__(self):
<<<<<<< Updated upstream
        return self.name
=======
        return self.country_name
>>>>>>> Stashed changes

class Meta:
    verbose_name = _("types")
    verbose_name_plural = _("types")
    ralated_name = ['country_name']


    def __str__(self):
<<<<<<< Updated upstream
        return self.name
=======
        return self.country_name
>>>>>>> Stashed changes

    def get_absolute_url(self):
        return reverse('types-detail', args=[str(self.id)])


class Review(models.Model):
    creator = models.ForeignKey(
        get_user_model(),
        verbose_name=('owner'),
        on_delete=models.SET_NULL,
        null=True, 
        blank=True
        )
    image = models.URLField(max_length=2000, help_text='Enter URL for beer image', blank=True, default='')
    name = models.CharField(max_length=200, help_text='Enter beer name')
    beertype = models.ForeignKey(Type, on_delete=models.SET_NULL, null=True)
    # Foreign Key used because beer can only have one type, but types of beer can be attributable to multiple beers
    # CASCADE TRINA VISKA ARBA SET_NULL VISAS PERZIURAS PADARYS BE ALAYS TIPO 
    RATINGS = (
        ('1', 'very bad'),
        ('2', 'bad'),
        ('3', 'average'),
        ('4', 'good'),
        ('5', 'perfect')
    )
    
    rating = models.CharField(max_length=1, choices=RATINGS, help_text='Choose beer rating')
    comments = models.TextField(max_length=500)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    
class Meta:
    verbose_name = _("review")
    verbose_name_plural = _("review")


    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
<<<<<<< Updated upstream
        return reverse('review_detail', kwargs={'pk': self.pk})
=======
        return reverse('review_detail', kwargs={'pk': self.pk})
>>>>>>> Stashed changes
