# -*- coding: utf-8 -*-

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ObjectDoesNotExist
from smart_selects.db_fields import ChainedForeignKey

from django.utils.safestring import mark_safe

from AnarWeb.apps.yacimientos.models import *


class ManifestacionYacimiento(models.Model):

    yacimiento = models.OneToOneField(Yacimiento, related_name='ManifestacionYacimiento')

    esGeoglifo = models.BooleanField('13.1. Geoglifo')
    esPintura = models.BooleanField('13.2. Pintura Rupestre')
    esPetroglifo = models.BooleanField('13.3. Petroglifo')
    esPetroglifoPintado = models.BooleanField('13.3.1. Petroglifo Pintado')
    esMicroPetroglifo = models.BooleanField('13.4. Micro-Petroglifo')
    esPiedraMiticaNatural = models.BooleanField('13.5. Piedra Mítica Natural')
    esCerroMiticoNatural = models.BooleanField('13.6. Cerro Mítico Natural')
    esCerroConPetroglifo = models.BooleanField('13.6.1. Con Petroglifo')
    esCerroConPintura = models.BooleanField('13.6.2. Con Pintura')
    esCerroConDolmen = models.BooleanField('13.6.3. Con Dolmen')
    esMonumentosMegaliticos = models.BooleanField('13.7. Monumentos Megalíticos')
    esMonolitos = models.BooleanField('13.7.1. Monolitos')
    esMonolitoConGrabados = models.BooleanField('13.7.1.1. Con Grabados')
    esMenhires = models.BooleanField('13.7.2. Menhires')
    esMenhiresConPuntos = models.BooleanField('13.7.2.1. Con Puntos Acoplados')
    esMenhiresConPetroglifo = models.BooleanField('13.7.2.2. Con Petroglifo')
    esMenhiresConPintura = models.BooleanField('13.7.2.3. Con Pintura')
    esAmolador = models.BooleanField('13.8. Amolador')
    esBatea = models.BooleanField('13.9. Batea')
    esPuntosAcoplados = models.BooleanField('13.10. Puntos Acoplados')
    esCupulas = models.BooleanField('13.11. Cupulas')
    esMortero = models.BooleanField('13.12. Mortero o Metate')
	
    abbr = 'tmy'

    def __unicode__(self):
        return '' # '# ' + str(self.id)
	
    def get_texto_descriptivo(self):
	
		"Genera un texto descriptivo de los tipos de manIfestacion que representa el objeto"				
		return  (
			('Geoglifo, ' if self.esGeoglifo else '') +
			('Pintura Rupestre, ' if self.esPintura else '') +
			('Petroglifo, ' if self.esPetroglifo else '' ) +
			('Petroglifo Pintado, ' if self.esPetroglifoPintado else '' ) +
			('Micro-Petroglifo, ' if self.esMicroPetroglifo else '' ) +
			('Piedra Mítica Natural, ' if self.esPiedraMiticaNatural else '' ) +
			('Cerro Mítico Natural, ' if self.esCerroMiticoNatural else '' ) + 
			('Cerro Mítico Natural Con Petroglifo, ' if self.esCerroConPetroglifo else '' ) +
			('Cerro Mítico Natural Con Pintura, ' if self.esCerroConPintura else '' ) +
			('Cerro Mítico Natural Con Dolmen, ' if self.esCerroConDolmen else '' ) +
			('Monumentos Megalíticos, ' if self.esMonumentosMegaliticos else '' ) +
			('Monolitos, ' if self.esMonolitos else '' ) +
			('Monolitos Con Grabados, ' if self.esMonolitoConGrabados else '' ) +
			('Menhires, ' if self.esMenhires else '' ) +
			('Menhires Con Puntos Acoplados, ' if self.esMenhiresConPuntos else '' ) +
			('Menhires Con Petroglifo, ' if self.esMenhiresConPetroglifo else '' ) + 
			('Menhires Con Pintura, ' if self.esMenhiresConPintura else '' ) + 
			('Amolador, ' if self.esAmolador else '' ) +
			('Batea, ' if self.esBatea else '' ) +	
			('Puntos Acoplados, ' if self.esPuntosAcoplados else '' ) +
			('Cúpulas, ' if self.esCupulas else '' ) +
			('Mortero o Metate ' if self.esMortero else '') 				
		)
	
    texto_descriptivo = property(get_texto_descriptivo)
	
    class Meta:
        verbose_name = '13. Tipo de Manifestación'
        verbose_name_plural = '13. Tipo de Manifestación'
	
    
class UbicacionYacimiento(models.Model):

    yacimiento = models.OneToOneField(Yacimiento, related_name='UbicacionYacimiento')
    
    enCerro = models.BooleanField('14.1. Cerro')
    enCerroCima = models.BooleanField('14.1.1. Cima')
    enCerroLadera = models.BooleanField('14.1.2. Ladera')
    enCerroFalda = models.BooleanField('14.1.3. Falda')
    enCerroFila = models.BooleanField('14.1.4. Fila')
    enCerroPieDeMonte = models.BooleanField('14.1.5. Pie de Monte')
    enCerroBarranco = models.BooleanField('14.1.6. Barranco')
    enCerroAcantilado = models.BooleanField('14.1.7. Acantilado')
    enValle = models.BooleanField('14.2. Valle')
    enRio = models.BooleanField('14.3. Río')
    enRioLecho = models.BooleanField('14.3.1. Lecho')
    enRioMargenDerecha = models.BooleanField('14.3.2. Margen Derecha')
    enRioMargenIzquierda = models.BooleanField('14.3.3. Margen Izquierda')
    enRioIsla = models.BooleanField('14.3.4. Isla')
    enRioRaudal = models.BooleanField('14.3.5. Raudal')
    enRioCosta = models.BooleanField('14.4. Costa')

    abbr = 'ubm'
        
    class Meta:
        verbose_name = '14. Ubicación'
        verbose_name_plural = '14. Ubicación'
    
    def __unicode__(self):
        return '' # '# ' + str(self.id)

class OrientacionYacimiento (models.Model):
    
    yacimiento = models.OneToOneField(Yacimiento, related_name='OrientacionYacimiento')

    haciaCerro = models.BooleanField('15.1. Hacia Cerro')
    haciaValle = models.BooleanField('15.2. Hacia Valle')
    haciaRio = models.BooleanField('15.3. Hacia Rio')
    haciaCosta = models.BooleanField('15.4. Hacia Costa')
    haciaCielo = models.BooleanField('15.5. Hacia Cielo')
    otros = models.CharField('15.6. Otros', blank = True, max_length=200)
    orientacion = models.CharField('15.7. Orientacion Cardinal', blank = True, max_length=200)
    
    abbr = 'oyc'

    class Meta:
        verbose_name = '15. Orientacion del Yacimiento'
        verbose_name_plural = '15. Orientacion del Yacimiento'
        
    def __unicode__(self):
        return '' # '# ' + str(self.id)

class MaterialYacimiento(models.Model):
    
    yacimiento = models.OneToOneField(Yacimiento, related_name='MaterialYacimiento')
        
    esRoca = models.BooleanField('22.1. Roca')
    esIgnea = models.BooleanField('22.1.1. Origen - Ignea')
    esMetamor= models.BooleanField('22.1.2. Origen - Metamórfica')
    esSedimentaria = models.BooleanField('22.1.3. Origen - Sedimentaria')
    tipo = models.CharField('22.1.4. Origen - Tipo', blank = True, max_length=200)
    esTierra = models.BooleanField('22.2. Tierra')
    esHueso = models.BooleanField('22.3. Hueso')
    esCorteza = models.BooleanField('22.4. Corteza de árbol')
    esPiel = models.BooleanField('22.5. Pieles')
    otros = models.CharField('22.6. Otros', blank = True, max_length=200)
    
    abbr = 'may'

    class Meta:
        verbose_name = '22. Material'
        verbose_name_plural = '22. Material'
        
    def __unicode__(self):
        return '' # '# ' + str(self.id) 
