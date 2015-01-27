# -*- coding: utf-8 -*-

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ObjectDoesNotExist
from smart_selects.db_fields import ChainedForeignKey

from django.utils.safestring import mark_safe

from ..models import Yacimiento


class ManifestacionesAsociadas(models.Model):

    yacimiento = models.OneToOneField(Yacimiento, related_name='ManifestacionesAsociadas')
	 
    esLitica = models.BooleanField('30.1. Lítica')
    descripcionLitica = models.CharField('30.1. Descripción Lítica', blank = True, max_length=500)
    esCeramica = models.BooleanField('30.2. Cerámica')
    descripcionCeramica = models.CharField('30.2. Descripción Cerámica', blank = True, max_length=500)
    esOseo = models.BooleanField('30.3. Oseo')
    descripcionOseo = models.CharField('30.3. Descripción Oseo', blank = True, max_length=500)
    esConcha = models.BooleanField('30.4. Concha')
    descripcionConcha = models.CharField('30.4. Descripción Concha', blank = True, max_length=500)
    esCarbon = models.BooleanField('30.5. Carbón No Superficial')
    descripcionCarbon = models.CharField('30.5. Descripción Carbón No Superficial', blank = True, max_length=500)
    esMito = models.BooleanField('30.6. Mitos')
    descripcionMito = models.CharField('30.6. Descripción Mitos', blank = True, max_length=500)
    esCementerio = models.BooleanField('30.7. Cementerios')
    descripcionCementerio = models.CharField('30.7. Descripción Cementerios', blank = True, max_length=500)
    esMonticulo = models.BooleanField('30.8. Montículos')
    descripcionMonticulo = models.CharField('30.8. Descripción Montículos', blank = True, max_length=500)
    otros = models.CharField('30.9. Otros', blank = True, max_length=500)
     
    abbr = 'mso'
 
    class Meta:
        verbose_name = '30. Manifestaciones Asociadas'
        verbose_name_plural = '30. Manifestaciones Asociadas'
         
    def __unicode__(self):
        return '' # '# ' + str(self.id)
		 
class ManifestacionesLitica(models.Model):

    yacimiento = models.OneToOneField(Yacimiento, related_name='ManifestacionesLitica')    
    esLitica = models.BooleanField('30.1. Lítica')
    descripcionLitica = models.CharField('Descripción', blank = True, max_length=500)
    
    abbr = 'mal'

    class Meta:
        verbose_name = '30. Manifestaciones Asociadas'
        verbose_name_plural = '30. Manifestaciones Asociadas'
        
    def __unicode__(self):
        return '' # '# ' + str(self.id)		

class ManifestacionesCeramica(models.Model):

    yacimiento = models.OneToOneField(Yacimiento, related_name='ManifestacionesCeramica')    
    esCeramica = models.BooleanField('30.2. Cerámica')
    descripcionCeramica = models.CharField('Descripción', blank = True, max_length=500)    
    
    abbr = 'mac'

    class Meta:
        verbose_name = '30. Manifestaciones Asociadas'
        verbose_name_plural = ''
        
    def __unicode__(self):
        return '' # '# ' + str(self.id)	

class ManifestacionesOseo(models.Model):

    yacimiento = models.OneToOneField(Yacimiento, related_name='ManifestacionesOseo')    
    esOseo = models.BooleanField('30.3. Oseo')
    descripcionOseo = models.CharField('Descripción', blank = True, max_length=500)

    abbr = 'mao'

    class Meta:
        verbose_name = '30. Manifestaciones Asociadas'
        verbose_name_plural = ''
        
    def __unicode__(self):
        return '' # '# ' + str(self.id)	
		
class ManifestacionesConcha(models.Model):

    yacimiento = models.OneToOneField(Yacimiento, related_name='ManifestacionesConcha')    
    esConcha = models.BooleanField('30.4. Concha')
    descripcionConcha = models.CharField('Descripción', blank = True, max_length=500)

    abbr = 'mco'

    class Meta:
        verbose_name = '30. Manifestaciones Asociadas'
        verbose_name_plural = ''
        
    def __unicode__(self):
        return '' # '# ' + str(self.id)	
		
class ManifestacionesCarbon(models.Model):

    yacimiento = models.OneToOneField(Yacimiento, related_name='ManifestacionesCarbon')    
    esCarbon = models.BooleanField('30.5. Carbón No Superficial')
    descripcionCarbon = models.CharField('Descripción', blank = True, max_length=500)

    abbr = 'mcar'

    class Meta:
        verbose_name = '30. Manifestaciones Asociadas'
        verbose_name_plural = ''
        
    def __unicode__(self):
        return '' # '# ' + str(self.id)	

class ManifestacionesMito(models.Model):

    yacimiento = models.OneToOneField(Yacimiento, related_name='ManifestacionesMito')    
    esMito = models.BooleanField('30.6. Mitos')
    descripcionMito = models.CharField('Descripción', blank = True, max_length=500)

    abbr = 'mami'

    class Meta:
        verbose_name = '30. Manifestaciones Asociadas'
        verbose_name_plural = ''
        
    def __unicode__(self):
        return '' # '# ' + str(self.id)			

class ManifestacionesCementerio(models.Model):

    yacimiento = models.OneToOneField(Yacimiento, related_name='ManifestacionesCementerio')    
    esCementerio = models.BooleanField('30.7. Cementerios')
    descripcionCementerio = models.CharField('Descripción', blank = True, max_length=500)

    abbr = 'macm'

    class Meta:
        verbose_name = '30. Manifestaciones Asociadas'
        verbose_name_plural = ''
        
    def __unicode__(self):
        return '' # '# ' + str(self.id)	

class ManifestacionesMonticulo(models.Model):

    yacimiento = models.OneToOneField(Yacimiento, related_name='ManifestacionesMonticulo')    
    esMonticulo = models.BooleanField('30.8. Montículos')
    descripcionMonticulo = models.CharField('Descripción', blank = True, max_length=500)

    abbr = 'mamn'

    class Meta:
        verbose_name = '30. Manifestaciones Asociadas'
        verbose_name_plural = ''
        
    def __unicode__(self):
        return '' # '# ' + str(self.id)	

class ManifestacionesOtros(models.Model):

    yacimiento = models.OneToOneField(Yacimiento, related_name='ManifestacionesOtros')    
    otros = models.CharField('30.9. Otros', blank = True, max_length=500)

    abbr = 'maot'

    class Meta:
        verbose_name = '30. Manifestaciones Asociadas'
        verbose_name_plural = ''
        
    def __unicode__(self):
        return '' # '# ' + str(self.id)		


class OtrosValores(models.Model):

    def __unicode__(self):
        return '' # '# ' + str(self.id) 
        

class OtrosValYac(OtrosValores):

    yacimiento = models.ForeignKey(Yacimiento, related_name='OtrosValYac')
    texto = models.CharField('33. Otros valores del sitio', blank = True, max_length=500)
    abbr = 'ovy'
    
    class Meta:
        verbose_name = 'Otros valores del sitio'
        verbose_name_plural = ''