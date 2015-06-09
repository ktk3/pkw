from django.db import models
from django.core.exceptions import ValidationError


class Wojewodztwo(models.Model):
    name = models.CharField(max_length=35)

    def __unicode__(self):
        return u"{}".format(self.name)

class Powiat(models.Model):
    name = models.CharField(max_length=35)
    woj = models.ForeignKey(Wojewodztwo)

    def __unicode__(self):
        return u"{}".format(self.name)

class Gmina(models.Model):
    name = models.CharField(max_length=35)
    powiat = models.ForeignKey(Powiat)

    def __unicode__(self):
        return u"{}".format(self.name)

class Okreg(models.Model):
    name = models.CharField(max_length=300)
    gmina = models.ForeignKey(Gmina)
    karty = models.IntegerField()
    wyborcy = models.IntegerField()
    modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u"{}".format(self.name)    

    def resave (self, dd, *args, **kwargs):
        if (int(self.karty) < 0) or (int(self.wyborcy) < 0):
            raise ValidationError('Niepoprawne dane. Sprobuj ponownie.')
        print "args ", args
        print "kwargs ", kwargs
        if self.modified > dd:
            raise ValidationError('Dane zmienily sie od odczytu. Sprobuj ponownie.')
        super(Okreg, self).save(*args, **kwargs)