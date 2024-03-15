from django.contrib.auth import get_user_model
from django.db import models 
from django.urls import reverse
from django.utils.translation import gettext as _

class Types(models.Model):
    """
    Model representing a specific beer type.
    """
    name = models.CharField(max_length=200, help_text='Enter name of a beer type')

    MAIN_TYPES = (
        ('w', 'Wheat beer'),
        ('l', 'Lager'),
        ('p', 'Pilsner'),
        ('i', 'IPA'),
        ('a', 'ALE'),
        ('s', 'Stout'),
        ('b', 'Bock'),
    )

    types = models.CharField(max_length=1, choices=MAIN_TYPES, null=True, blank=True, help_text='Chose your type of beer!')

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


class Meta:
    verbose_name = _("types")
    verbose_name_plural = _("types")
    ralated_name = ['name']


    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.name

    def get_absolute_url(self):
        """
        Returns the url to access a particular beer instance.
        """
        return reverse('types-detail', args=[str(self.id)])


class Review(models.Model):
    """
    Model representing a specific beer review of a specific user.
    """
    creator = models.ForeignKey(
        get_user_model(),
        verbose_name=('owner'),
        on_delete=models.SET_NULL,
        null=True, 
        blank=True
        )
    image = models.URLField(max_length=2000, help_text='Enter URL for beer image', blank=True, default='')
    name = models.CharField(max_length=200, help_text='Enter beer name')
    beertype = models.ForeignKey(Types, on_delete=models.SET_NULL, null=True)
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


class Meta:
    verbose_name = _("review")
    verbose_name_plural = _("review")


    
    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.name

    def get_absolute_url(self):
        """
        Returns the url to access a particular beer instance.
        """
        return reverse('review-detail', args=[str(self.id)])
