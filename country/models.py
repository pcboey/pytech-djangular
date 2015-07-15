from django.db import models

class Country(models.Model):
    iso = models.CharField('ISO Code', max_length=2)
    name = models.CharField('Country name', max_length=30)
    show = models.BooleanField(default=True)

    def __unicode__(self):
        return '%s' % self.name

    class Meta:
        ordering = ('name',)
        verbose_name_plural = "countries"

class City(models.Model):
    country =  models.ForeignKey(Country)
    city = models.CharField(max_length=38)
    show = models.BooleanField(default=True)

    def __unicode__(self):
        return '%s' % self.city

    class Meta:
        ordering = ('city',)
        verbose_name_plural = "cities"
    
