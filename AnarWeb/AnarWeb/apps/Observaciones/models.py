# -*- coding: utf-8 -*-

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ObjectDoesNotExist
from smart_selects.db_fields import ChainedForeignKey

from django.utils.safestring import mark_safe

from ..models import Yacimiento

class Observaciones(models.Model):

    texto = models.CharField('34.1. Observaciones', max_length=500)
	
    def __unicode__(self):
        return '' # '# ' + str(self.id)	

class ObservacionesYac(Observaciones):

    yacimiento = models.ForeignKey(Yacimiento, related_name='ObservacionesYac')
    
    abbr = 'oya'
    
    class Meta:
        verbose_name = 'Observaciones'
        verbose_name_plural = '34. Observaciones'



class LlenadoPor(models.Model):

    nombre = models.CharField('35.1. Llenada por: ', blank = True, max_length=200)
    fecha = models.CharField('35.2. Fecha', blank = True, null= True, max_length=100)
    def __unicode__(self):
        return '' # '# ' + str(self.id)	

class LlenadoYac(LlenadoPor):    

    yacimiento = models.ForeignKey(Yacimiento, related_name='LlenadoYac')
    
    abbr = 'ypy'

    class Meta:
        verbose_name = 'Ficha llenada por'
        verbose_name_plural = '35. Ficha llenada Por'


class SupervisadoPor(models.Model):

    nombre = models.CharField('36.1. Supervisada por: ', blank = True, max_length=200)
    fecha = models.CharField('36.2. Fecha', blank = True, null= True, max_length=100)
	
    def __unicode__(self):
        return '' # '# ' + str(self.id)	

class SupervisadoYac(SupervisadoPor):
    
    yacimiento = models.ForeignKey(Yacimiento, related_name='SupervisadoYac')
    
    abbr = 'spy'
    
    class Meta:
        verbose_name = 'Ficha Supervisada Por'
        verbose_name_plural = '36. Ficha Supervisada Por'