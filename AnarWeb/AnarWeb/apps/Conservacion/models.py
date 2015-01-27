# -*- coding: utf-8 -*-

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ObjectDoesNotExist
from smart_selects.db_fields import ChainedForeignKey

from django.utils.safestring import mark_safe

from ..models import Yacimiento

class EstadoConserYac(models.Model):

    yacimiento = models.OneToOneField(Yacimiento, related_name='EstadoConserYac')
   
    enBuenEstado = models.BooleanField('27.1. Bueno')
    estadoModificado = models.BooleanField('27.2. Modificado')
    trasladado = models.IntegerField('27.2.1. Trasladado', blank = True, null = True,
                                    validators=[MinValueValidator(1), MaxValueValidator(2)] )
    trasladadoPa = models.CharField('27.2.1. Trasladado Pa(s) Nro ', blank = True, max_length=200)
    sumergido = models.IntegerField('27.2.2. Sumergido', blank = True, null = True,
                                    validators=[MinValueValidator(1), MaxValueValidator(2)] )
    sumergidoPa = models.CharField('27.2.2. Sumergido Pa(s) Nro ', blank = True, max_length=200)
    enterrado = models.IntegerField('27.2.3. Enterrado', blank = True, null = True,
                                    validators=[MinValueValidator(1), MaxValueValidator(2)] )
    enterradoPa = models.CharField('27.2.3. Enterrado Pa(s) Nro ', blank = True, max_length=200)
    perdido = models.IntegerField('27.2.4. Perdido', blank = True, null = True,
                                    validators=[MinValueValidator(1), MaxValueValidator(2)] )
    perdidoPa = models.CharField('27.2.4. Perdido Pa(s) Nro ', blank = True, max_length=200)
    destruido = models.IntegerField('27.2.5. Destruido', blank = True, null = True,
                                     validators=[MinValueValidator(1), MaxValueValidator(2)] )
    destruidoPa = models.CharField('27.2.5. Destruido Pa(s) Nro ', blank = True, max_length=200)
    crecimientoVeg = models.IntegerField('27.2.6. Crecimiento Vegetal', blank = True, null = True,
                                        validators=[MinValueValidator(1), MaxValueValidator(2)] )
    crecimientoVegPa = models.CharField('27.2.6. Crecimiento Vegetal Pa(s) Nro ', blank = True, max_length=200)
    patina = models.IntegerField('27.2.7. Pátina', blank = True, null = True,
                                    validators=[MinValueValidator(1), MaxValueValidator(2)] )
    patinaPa = models.CharField('27.2.7. Pátina Pa(s) Nro ', blank = True, max_length=200)
    erosion = models.IntegerField('27.2.8. Erosión ', blank = True, null = True,
                                     validators=[MinValueValidator(1), MaxValueValidator(2)] )
    erosionPa = models.CharField('27.2.8. Erosión Pa(s) Nro ', blank = True, max_length=200)
    
    estaDestruido = models.BooleanField('27.3. Grado de Destrucción del Sitio')
    esPorCausaNatural = models.BooleanField('27.3.1. Natural')
    enPorCausaNaturalLigera = models.BooleanField('27.3.1.1. Ligera')
    enPorCausaNaturalAguda = models.BooleanField('27.3.1.2. Aguda')
    enPorCausaHumana = models.BooleanField('27.3.2. Humana')
    enPorCausaHumanaLigera = models.BooleanField('27.3.2.1. Ligera')
    enPorCausaHumanaAguda = models.BooleanField('27.3.2.1. Aguda')
    especificar = models.CharField('27.4. Especificar Causa y Efecto', blank = True, max_length=500)
    destruccionPotencial = models.BooleanField('27.5. Destrucción Potencial del Sitio')
    
    abbr = 'ecy'

    class Meta:
        verbose_name = '27. Estado de la Conservación'
        verbose_name_plural = '27. Estado de la Conservación'
        
    def __unicode__(self):
        return '' # '# ' + str(self.id)

class CausasDestruccionYac(models.Model):

    yacimiento = models.OneToOneField(Yacimiento, related_name='CausasDestruccionYac')
	
    porAsentamientoHumand = models.BooleanField('27.5.1. Asentamiento Humano')
    porObraCortoPlazo = models.BooleanField('27.5.2. Obra Infraestructura a Corto Plazo')
    porObraMedianoPlazo = models.BooleanField('27.5.3. Obra Infraestructura a Mediano Plazo')
    porObraLargoPlazo = models.BooleanField('27.5.4. Obra Infraestructura a Largo Plazo')
    porNivelacion = models.BooleanField('27.5.5. Nivelación del Terreno Como Obra Agrícola')
    porExtraccionFamiliar = models.BooleanField('27.5.6. Extracción Como Actividad Familiar')
    porExtraccionMayor = models.BooleanField('27.5.7. Extracción Como Actividad Mayor')
    porVandalismo = models.BooleanField('27.5.8. Vandalismo')
    porErosion = models.BooleanField('27.5.9. Erosión' , 
                                     help_text=("Desgaste de la piedra producido por efectos climatológicos."))
    porErosionParModerada = models.BooleanField('27.5.9.1. Erosión Parcial Moderada')
    porErosionParSevera = models.BooleanField('27.5.9.2. Erosión Parcial Severa')
    porErosionExtModerada = models.BooleanField('27.5.9.3. Erosión Extensiva Moderada')
    porErosionExtSevera = models.BooleanField('27.5.9.4. Erosión Extensiva Severa')
    otros = models.CharField('27.5.10  Otros', blank = True, max_length=500)
	
    abbr = 'cdy'

    class Meta:
        verbose_name = '27.5.1. Causas'
        verbose_name_plural = '27.5.1. Causas'
        
    def __unicode__(self):
        return '' # '# ' + str(self.id)

class IntensidadDestruccionYac(models.Model):

    yacimiento = models.OneToOneField(Yacimiento, related_name='IntensidadDestruccionYac')
    observaciones = models.CharField('27.6. Observaciones Sobre Intensidad de Destrucción del Sitio, y Otros Procesos No Descritos', blank = True, max_length=200)	
    esDeTiempo = models.BooleanField('27.6.1. Tiempo')
    esInmediato = models.BooleanField('27.6.1.1. Inmediato')
    unAno = models.BooleanField('27.6.1.2. Un Año')
    dosAno = models.BooleanField('27.6.1.3.  Dos Años')
    tresAno = models.BooleanField('27.6.1.4. Tres Años')
    cuatroAno = models.BooleanField('27.6.1.5. Cuatro Años')
    cincoAno = models.BooleanField('27.6.1.6. Cinco Años')
    mas = models.CharField('27.6.1.7. Más', blank = True, max_length=500)
	
    abbr = 'idy'

    class Meta:
        verbose_name = '27.6.1. Tiempo'
        verbose_name_plural = ''
        
    def __unicode__(self):
        return '' # '# ' + str(self.id)
	
class ConsiderTemp(models.Model):
    
    yacimiento = models.OneToOneField(Yacimiento, related_name='ConsiderTemp')
    
    cincoAno = models.BooleanField('28.1. Patina')
    otros = models.CharField('28.2. Otros', blank = True, max_length=500)
    
    abbr = 'tem'
        
    class Meta:
        verbose_name = '28. Consideración sobre Temporalidad'
        verbose_name_plural = '28. Consideración sobre Temporalidad'
    
    def __unicode__(self):
        return '' # '# ' + str(self.id)

class CronologiaTentativa(models.Model):
    
    yacimiento = models.ForeignKey(Yacimiento, related_name='CronologiaTentativa')
    
    esCrono1 = models.BooleanField('29.1. Anterior a 5000 a.p.')
    esCrono2 = models.BooleanField('29.2. 5000 - 1500 a.p.')
    esCrono3 = models.BooleanField('29.3. 1500 a.p. - 200 n.e.')
    esCrono4 = models.BooleanField('29.4. 200 - 650/900 n.e.')
    esCrono5 = models.BooleanField('29.5. 650/900 - 1200 n.e.')
    esCrono6 = models.BooleanField('29.6. 1200 - 1521 n.e.')
    esCrono7 = models.BooleanField('29.7. Post 1521 n.e.')
    autor = models.CharField('29.8.  Autor', blank = True, max_length=200)
    fecha = models.CharField('29.8.1. Fecha', blank = True, max_length=200)
    institucion = models.CharField('29.8.2. Institución', blank = True, max_length=200)
    pais = models.CharField('29.8.3. País', blank = True, max_length=200)
    direccion = models.CharField('29.8.4. Dirección', blank = True, max_length=200)
    telefono = models.CharField('29.8.5. Tel/Fax', blank = True, max_length=200)
    mail = models.CharField('29.8.6. Correo Electrónico', blank = True, max_length=200)
    tecnica = models.CharField('29.8.7. Técnica', blank = True, max_length=200)
    bibliografia = models.CharField('29.8.8. Bibliografía', blank = True, max_length=200)
    twitter = models.CharField('29.8.9. Twitter', blank = True, max_length=200)
    facebook = models.CharField('29.8.10. Facebook', blank = True, max_length=200)

    abbr = 'cte'
    
    class Meta:
        verbose_name = '29. Cronología Tentativa'
        verbose_name_plural = '29. Cronología Tentativa'
    
    def __unicode__(self):
        return '' # '# ' + str(self.id)
