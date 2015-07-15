from django.db import models
from django.core.urlresolvers import reverse

from country.models import Country, City

class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    country = models.ForeignKey(Country)
    city = models.ForeignKey(City)
    website = models.URLField()
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ["name"]

    def __unicode__(self):  
        return self.name

    def get_absolute_url(self):
        return reverse('publisher-detail', kwargs={'pk': self.pk})

class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    headshot = models.ImageField(upload_to='author_headshots', blank=True)

    def __unicode__(self): 
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField('Author')
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField()

    def __unicode__(self): 
        return self.title
