# -*- coding: utf-8 -*-

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ObjectDoesNotExist
from smart_selects.db_fields import ChainedForeignKey

from django.utils.safestring import mark_safe

from ..models import Yacimiento

class LocalidadYacimiento(models.Model):
    
    yacimiento = models.OneToOneField(Yacimiento, related_name='LocalidadYacimiento')
    
    esCentroPoblado = models.BooleanField('4.1. Centro de Poblado')
    esUrbano = models.BooleanField('4.1.1. Urbano')
    esRural = models.BooleanField('4.1.2. Rural')
    esIndigena = models.BooleanField('4.1.3. Indigena')
    nombrePoblado = models.CharField('4.1.4. Nombre', blank = True, max_length=200)
    esCentroNoPoblado = models.BooleanField('4.2. No Poblado')
    nombreNoPoblado = models.CharField('4.2.1. Nombre', blank = True, max_length=200)

    abbr = 'loc'

    def __unicode__(self):
        return '' # '# ' + str(self.id)
            
    class Meta:
        verbose_name = '4. Localidad'
        verbose_name_plural = '4. Localidad'
		
class UsoActSuelo(models.Model):

    yacimiento = models.OneToOneField(Yacimiento, related_name='UsoActSuelo')
    
    esForestal = models.BooleanField('5.1. Forestal')
    esGanadero = models.BooleanField('5.2. Ganadero')
    esAgriRiesgo = models.BooleanField('5.3. Agricultura de Riesgo')
    esAgriTemp = models.BooleanField('5.4. Agricultura Temporal')
    esSueloUrbano = models.BooleanField('5.5. Urbano')
    esSueloTuristico = models.BooleanField('5.6. Turístico')
    
    abbr = 'uas'

    class Meta:
        verbose_name = '5. Uso Actual Del Suelo'
        verbose_name_plural = '5. Uso Actual Del Suelo'
    
    def __unicode__(self):
        return '' # '# ' + str(self.id)

class TenenciaDeTierra(models.Model):
    
    yacimiento = models.OneToOneField(Yacimiento, related_name='TenenciaDeTierra')
   
    esPrivada = models.BooleanField('5.7.1. Privada')
    esComunal = models.BooleanField('5.7.2. Comunal')
    esEjido = models.BooleanField('5.7.3. Ejido')
    esMunicipal = models.BooleanField('5.7.4. Municipal')
    esABRAE = models.BooleanField('5.7.5. ABRAE (Área Bajo Régimen Especial)')
    esTenenciaOtros = models.CharField('5.7.6. Otros', blank = True,max_length=200)
    
    abbr = 'tdt'
    
    class Meta:
        verbose_name = '5.7 Tenencia de la Tierra'
        verbose_name_plural = '5.7 Tenencia de la Tierra'

    def __unicode__(self):
        return '' # '# ' + str(self.id)

class Indicaciones(models.Model):
 
    yacimiento = models.OneToOneField(Yacimiento, related_name='Indicaciones')
    
    direcciones = models.CharField('6. Indicaciones para llegar al Yacimiento', blank = True, max_length=200) 
    puntoDatum = models.CharField('6.1 Punto Datum ', blank = True, max_length=200)
    
    abbr = 'ind'
    
    class Meta:
        verbose_name = '6. Indicaciones para llegar al Yac' #aqui cambiar!!!!
        verbose_name_plural = '6. Indicaciones para llegar al Yac'

    def __unicode__(self):
        return '' # '# ' + str(self.id)

class Croquis (models.Model):

    yacimiento = models.ForeignKey(Yacimiento, related_name='Croquis')
    archivo = models.ImageField('6.2. Esquema de llegada - Archivo', upload_to='esquema/%Y_%m', null=True, blank=True)
    
    abbr = 'crq'

    class Meta:
        verbose_name = '..'
        verbose_name_plural = ''

    def __unicode__(self):
        return '' # '# ' + str(self.id)

class Plano (models.Model):
    
    yacimiento = models.OneToOneField(Yacimiento, related_name='Plano')
    numeroPlano = models.CharField('7. Número de plano', blank = True, max_length=200)
    abbr = 'pln'

    class Meta:
        verbose_name = '7. Número de Plano'
        verbose_name_plural = '7. Número de Plano'
    
    def __unicode__(self):
        return '' # '# ' + str(self.id)

 
class Coordenadas (models.Model):
    
    yacimiento = models.OneToOneField(Yacimiento, related_name='Coordenadas')
    
    longitud = models.CharField('8. Long. O(W)', blank = True, max_length=200)
    latitud = models.CharField('8. Lat. N', blank = True, max_length=200)
    utmAdicional = models.CharField('8. Utm Adicional', blank = True, max_length=200)
    
    abbr = 'crd'

    class Meta:
        verbose_name = '8. Coordenadas'
        verbose_name_plural = '8. Coordenadas'

    def __unicode__(self):
        return '' # '# ' + str(self.id)

class Datum (models.Model):
    
    OPCIONES_DATUM = (
        (1, '9.1 WGS 84'),
        (2, '9.2 La Canoa - Provisional Suramérica 1956'),
    ) 
     
    yacimiento = models.OneToOneField(Yacimiento, related_name='Datum')    
    tipoDatum = models.IntegerField('9. Datum GPS',choices = OPCIONES_DATUM, blank = True,null = True)
    
    abbr = 'dtm'

    class Meta:
        verbose_name = '9. Datum GPS'
        verbose_name_plural = '9. Datum GPS'

    def __unicode__(self):
        return '' # '# ' + str(self.id) 

class Altitud (models.Model):
    
    yacimiento = models.OneToOneField(Yacimiento, related_name='Altitud')

    texto = models.CharField('10.0. Texto', blank = True, max_length=200)   
    altura = models.CharField('10.1. Altura en mts', blank = True, max_length=200)
    superficie = models.CharField('10.2. Superficie en m2', blank = True, max_length=200)
    desarrollo = models.CharField('10.3. Desarrollo', blank = True, max_length=200)
    desnivel = models.CharField('10.4. Desnivel', blank = True, max_length=200)
    abbr = 'atd'  

    class Meta:
        verbose_name = '10. Altitud'
        verbose_name_plural = '10. Altitud'

    def __unicode__(self):
        return '' # '# ' + str(self.id)

class FotografiaYac (models.Model):
    
    yacimiento = models.ForeignKey(Yacimiento, related_name='FotografiaYac')
       
    esAerea = models.BooleanField('11. Aerea')
    noEsAerea = models.BooleanField('11. No Aerea')
    esSatelital = models.BooleanField('11. Satelital')
    fecha = models.CharField('11. Fecha', blank = True, null= True, max_length=100)	
    archivo = models.ImageField('11. Fotografía - Archivo', upload_to='yacimiento/%Y_%m', null=True, blank=True)
    
    abbr = 'fty'  

    class Meta:
        verbose_name = '11. Fotografia'
        verbose_name_plural = '11. Fotografias'

    def __unicode__(self):
        return '' # '# ' + str(self.id)

class TipoYacimiento (models.Model):
    
    yacimiento = models.OneToOneField(Yacimiento, related_name='TipoYacimiento')

    esParedRocosa = models.BooleanField('12.1. Pared Rocosa')
    esRoca = models.BooleanField('12.2. Roca')
    esDolmen = models.BooleanField('12.3. Dolmen(natural)')
    esAbrigo = models.BooleanField('12.4. Abrigo')
    esCueva = models.BooleanField('12.5. Cueva')
    esCuevadeRec = models.BooleanField('12.6. Cueva de Recubrimiento')
    esTerrenoSup = models.BooleanField('12.7. Terreno Superficial')
    esTerrenoPro = models.BooleanField('12.8. Terreno Profundo')
    
    abbr = 'tyc'

    class Meta:
        verbose_name = '12. Tipo de Yacimiento'
        verbose_name_plural = '12. Tipo de Yacimiento'
        
    def __unicode__(self):
        return '' # '# ' + str(self.id)