# -*- coding: utf-8 -*-

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ObjectDoesNotExist
from smart_selects.db_fields import ChainedForeignKey

from django.utils.safestring import mark_safe

########################################################################################
# Clases modificadas
########################################################################################

def short_text(text):
	""" Retorna un string limitado para evitar que los toString se vean muy largos"""
	return text[0:100]

class CharField(models.CharField):
	
	"""Tipo de Dato implementado para evitar que los campos títulos y textos se 
	vean limitados, al utilizar el tipo de datos de postgre 'text' que es sin limite."""

	def __init__(self, *args, **kwargs):
		kwargs.setdefault('max_length', 65000)
		super(CharField, self).__init__(*args, **kwargs)

	def db_type(self, connection):
		return 'text'

	def south_field_triple(self):
		"""Only necessary if using South migrations, which you should."""
		from south.modelsinspector import introspector
		field_class = self.__class__.__module__ + "." + self.__class__.__name__
		args, kwargs = introspector(self)
		return (field_class, args, kwargs)
		
########################################################################################
# Diagrama de yacimiento
########################################################################################

class Estado(models.Model):
        
    nombre = CharField('3. Estado/Provincia')
    activo = models.IntegerField('Activo', validators=[MinValueValidator(0), MaxValueValidator(1)])
     
    #representacion en string de un objeto de tipo estado
    def __unicode__(self):
        return self.nombre
        	
    abbr = 'edo'

    class Meta:
        verbose_name = '3. Estado/Provincia'
        verbose_name_plural = '3. Estado/Provincia'

class Municipio(models.Model):
        
    nombre = CharField('2. Municipio')
    estado = models.ForeignKey(Estado, related_name='Municipio')	
    activo = models.IntegerField('Activo', validators=[MinValueValidator(0), MaxValueValidator(1)])
    
    #representacion en string de un objeto de tipo municipio
    def __unicode__(self):
        return self.nombre
        	
    abbr = 'mpio'

    class Meta:
        verbose_name = '2. Municipio'
        verbose_name_plural = '2. Municipios'		
		


class Yacimiento(models.Model):
       
    codigo = models.CharField('(00). Codigo ANAR', unique = True, max_length=20)
    pais = CharField('0. Pais',  default = 'Venezuela')
    nombre = CharField('1. Nombre(s) del Yacimiento')
    municipio = CharField('2. Municipio')    
    estado = CharField('3. Estado/Provincia')    
     
    #representacion en string de un objeto tipo Yacimiento
    def __unicode__(self):
        return short_text('PB1-' + self.codigo + '-' + self.nombre)
        
    def _get_tipo_manifestaciones(self):
    
        "Determina los tipos de manifestaciones presentes en un yacimiento"
        try :
            manifestacion = ManifestacionYacimiento.objects.get(yacimiento=self.id)
            return manifestacion.texto_descriptivo
        except ObjectDoesNotExist:
            return '';
            
    tipos_de_manifestaciones = property(_get_tipo_manifestaciones, '13. Tipo de Manifestación')
    
    abbr = 'yac'

    class Meta:
        verbose_name = 'Yacimiento'
        verbose_name_plural = 'Yacimientos'
        

class TexturaSuelo (models.Model):
    
    yacimiento = models.OneToOneField(Yacimiento, related_name='TexturaSuelo')

    esRocaMadre = models.BooleanField('16.1. Roca Madre')
    esPedregoso = models.BooleanField('16.2. Pedregoso')
    esArenoso = models.BooleanField('16.3. Arenoso')
    esArcilloso = models.BooleanField('16.4. Arcilloso')
    mixto = CharField('16.5. Mixto', blank = True)
    
    abbr = 'tsl'

    class Meta:
        verbose_name = '16. Textura del Suelo'
        verbose_name_plural = '16. Textura del Suelo'
        
    def __unicode__(self):
        return '' # '# ' + str(self.id)

class FloraYacimiento (models.Model):

    yacimiento = models.OneToOneField(Yacimiento, related_name='FloraYacimiento')    
    flora = CharField('17. Flora', blank = True)
    
    abbr = 'fly'

    class Meta:
        verbose_name = '17. Flora'
        verbose_name_plural = '17. Flora'
        
    def __unicode__(self):
        return '' # '# ' + str(self.id)

class FaunaYacimiento (models.Model):
    
    yacimiento = models.OneToOneField(Yacimiento, related_name='FaunaYacimiento')
    fauna = CharField('18. Fauna', blank = True)
    
    abbr = 'fay'
    
    class Meta:
        verbose_name = '18. Fauna'
        verbose_name_plural = '18. Fauna'
        
    def __unicode__(self):
        return '' # '# ' + str(self.id)

class HidrologiaYacimiento (models.Model):

    yacimiento = models.OneToOneField(Yacimiento, related_name='HidrologiaYacimiento')
    
    rio = models.BooleanField('19.1. Rio')
    laguna = models.BooleanField('19.2. Laguna')
    arroyo = models.BooleanField('19.3. Arroyo')
    arroyoPerenne= models.BooleanField('19.3.1. Perenne')
    manantial = models.BooleanField('19.4. Manantial')
    manantialIntermitente = models.BooleanField('19.4.1. Intermitente')
    otros = CharField('19.5. Otros', blank = True)
    nombre = CharField('19.6. Nombre', blank = True)
    distancia = CharField('19.7. Distancia al Yacimiento', blank = True)
    observaciones = CharField('19.8. Observaciones', blank = True)
    
    abbr = 'hiy'

    class Meta:
        verbose_name = '19. Hidrología'
        verbose_name_plural = '19. Hidrología'
        
    def __unicode__(self):
        return '' # '# ' + str(self.id)

class TipoExposicionYac(models.Model):

    yacimiento = models.OneToOneField(Yacimiento, related_name='TipoExposicionYac')
    
    expuesto = models.BooleanField('20.1. Expuesto')
    noExpuesto = models.BooleanField('20.2. No Expuesto')
    expuestoPeriodicamente = models.BooleanField('20.3. Expuesto Periódicamente')
    observaciones = CharField('20.4. Observaciones', blank = True)
    
    abbr = 'tey'

    class Meta:
        verbose_name = '20. Exposición'
        verbose_name_plural = '20. Exposición'

    def __unicode__(self):
        return '' # '# ' + str(self.id)

class ConstitucionYacimiento (models.Model):

    yacimiento = models.OneToOneField(Yacimiento, related_name='ConstitucionYacimiento')
    
    nroPiedras = models.IntegerField('21.1. Nro de Piedras en el Yacimiento Original', blank = True, null = True, )
    nroPiedrasGrabadas = models.IntegerField('21.1.1. Nro de Piedras Grabadas', blank = True, null = True, )
    nroPiedrasPintadas = models.IntegerField('21.1.2. Nro de Piedras Pintadas', blank = True, null = True, )
    nroPiedrasColocadas = models.IntegerField('21.1.3. Nro Piedras Colocadas', blank = True, null = True, )
    otros = CharField('21.2. Otros', blank = True)
    
    abbr = 'cny'

    class Meta:
        verbose_name = '21. Constitución del Yacimiento'
        verbose_name_plural = '21. Constitución del Yacimiento'
        
    def __unicode__(self):
        return '' # '# ' + str(self.id)




	
