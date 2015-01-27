# -*- coding: utf-8 -*-

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ObjectDoesNotExist
from smart_selects.db_fields import ChainedForeignKey

from django.utils.safestring import mark_safe

from ..models import Yacimiento

class TecnicaParaGeoglifo (models.Model):
    
    yacimiento = models.OneToOneField(Yacimiento, related_name='TecnicaParaGeoglifo')
    esGeoflifo = models.BooleanField('13.1. Geoflifo')
    tecnicas = models.CharField('23.1. Técnicas de Construcción', blank = True, max_length=500)
    
    abbr = 'tge'
    
    class Meta:
        verbose_name = '13.1. Geoflifo'
        verbose_name_plural = '23. Técnicas'
        
    def __unicode__(self):
        return '' # '# ' + str(self.id)

class TecnicaParaPintura (models.Model):
 
    yacimiento = models.OneToOneField(Yacimiento, related_name='TecnicaParaPintura')
    
    esPintura = models.BooleanField('13.2. Pintura Rupestre')
    conDedo = models.BooleanField('23.2. Dedo')
    fibra = models.BooleanField('23.3. Fibra')
    soplado = models.BooleanField('23.4. Soplado')
    otros = models.CharField('23.5. Otros', blank = True, max_length=500)
    
    abbr = 'tpi'

    class Meta:
        verbose_name = '13.2. Pintura Rupestre'
        verbose_name_plural = ''
        
    def __unicode__(self):
        return '' # '# ' + str(self.id)    

class TecnicaParaPetroglifo (models.Model):
 
    yacimiento = models.OneToOneField(Yacimiento, related_name='TecnicaParaPetroglifo')
    
    esPetroglifo = models.BooleanField('13.3. Petroglifo')
    esGrabado = models.BooleanField('23.6. Grabado')
    esGrabadoPercusion = models.BooleanField('23.6.1. Percusión')
    esGrabadoPercusionDirecta = models.BooleanField('23.6.1.1. Directa')
    esGrabadoPercusionIndirecta = models.BooleanField('23.6.1.2. Indirecta')
    esAbrasion = models.BooleanField('23.6.2. Abrasión')
    esAbrasionPiedra = models.BooleanField('23.6.2.1. Piedra')
    esAbrasionArena = models.BooleanField('23.6.2.2. Arena')
    esConcha = models.BooleanField('23.6.2.3. Concha')
    otros = models.CharField('23.6.3. Otros', blank = True, max_length=500)
    
    abbr = 'tpe'

    class Meta:
        verbose_name = '13.3 Petroglifo'
        verbose_name_plural = ''
        
    def __unicode__(self):
        return '' # '# ' + str(self.id)

class TecnicaParaMicroPetro (models.Model):

    yacimiento = models.OneToOneField(Yacimiento, related_name='TecnicaParaMicroPetro')
    
    esMicro = models.BooleanField('13.4. Micro-Petroglifo')
    esGrabado = models.BooleanField('23.6. Grabado')
    esGrabadoPercusion = models.BooleanField('23.6.1. Percusión')
    esGrabadoPercusionDirecta = models.BooleanField('23.6.1.1. Directa')
    esGrabadoPercusionIndirecta = models.BooleanField('23.6.1.2. Indirecta')
    esAbrasion = models.BooleanField('23.6.2. Abrasión')
    esAbrasionPiedra = models.BooleanField('23.6.2.1. Piedra')
    esAbrasionArena = models.BooleanField('23.6.2.2. Arena')
    esConcha = models.BooleanField('23.6.2.3. Concha')
    otros = models.CharField('23.6.3. Otros', blank = True, max_length=500)
    
    abbr = 'tmi'

    class Meta:
        verbose_name = '13.4. Micro-Petroglifo'
        verbose_name_plural = ''
        
    def __unicode__(self):
        return '' # '# ' + str(self.id)

class TecnicaParaMonumentos (models.Model):

    yacimiento = models.OneToOneField(Yacimiento, related_name='TecnicaParaMonumentos')
    
    esMonumento = models.BooleanField('13.7. Monumentos Megalíticos')
    esMonolito = models.BooleanField('13.7.1 Monolitos')
    esMenhir = models.BooleanField('13.7.2 Menhires')
    esDolmen = models.BooleanField('13.7.3 Dolmen (artificial)')
    tecnicas = models.CharField('23.7. Técnicas de Construcción', blank = True, max_length=500)
    otros = models.CharField('23.8. Otros', blank = True, max_length=500)
    
    abbr = 'tmo'

    class Meta:
        verbose_name = '13.7. Monumentos Megalíticos'
        verbose_name_plural = ''
        
    def __unicode__(self):
        return '' # '# ' + str(self.id)

class CaracSurcoPetroglifo (models.Model):
    
    yacimiento = models.OneToOneField(Yacimiento, related_name='CaracSurcoPetroglifo')
    
    anchoDe = models.CharField('24.1. Ancho desde (en cm)', blank = True, max_length=200)
    anchoA = models.CharField('24.1. Ancho hasta (en cm)', blank = True, max_length=200)
    produndidadDe = models.CharField('24.2. Profundidad desde (en cm)', blank = True, max_length=200)
    profundidadA = models.CharField('24.2. Profundidad hasta (en cm)', blank = True, max_length=200)
    esBase = models.BooleanField('24.3. Base')
    esBaseRedonda = models.BooleanField('24.3.1. Redonda')
    esBaseAguda = models.BooleanField('24.3.2. Aguda')
    esBajoRelieve = models.BooleanField('24.4. Bajo Relieve')
    esBajoRelieveLineal = models.BooleanField('24.4.1. Lineal')
    esBajoRelievePlanar = models.BooleanField('24.4.2. Planar')
    esAltoRelieve = models.BooleanField('24.5. Alto Relieve')
    esAltoRelieveLineal = models.BooleanField('24.5.1. Lineal')
    esAltoRelievePlanar = models.BooleanField('24.5.2. Planar')
    esAreaInterlineal = models.BooleanField('24.6. Áreas Interlineales')
    esAreaInterlinealPulida = models.BooleanField('24.6.1. Pulidas')
    esAreaInterlinealRebajada = models.BooleanField('24.6.2. Rebajadas')
    esGrabadoSuperpuesto = models.BooleanField('24.7. Grabados Superpuestos')
    esGrabadoRebajado = models.BooleanField('24.8. Grabados Rebajados')
    
    abbr = 'cpe'

    class Meta:
        verbose_name = '13.3. Petroglifo'
        verbose_name_plural = '24. Características del surco grabado'
        
    def __unicode__(self):
        return '' # '# ' + str(self.id)

class CaracSurcoAmoladores(models.Model):

    yacimiento = models.OneToOneField(Yacimiento, related_name='CaracSurcoAmoladores')
        
    largo = models.CharField('24.9. Largo (en cm)', blank = True, max_length=200)
    ancho = models.CharField('24.10. Ancho (en cm)', blank = True, max_length=200)
    diametro = models.CharField('24.11. Diámetro (en cm)', blank = True, max_length=500)
    
    abbr = 'cam'

    class Meta:
        verbose_name = '13.9. Amoladores'
        verbose_name_plural = ''
        
    def __unicode__(self):
        return '' # '# ' + str(self.id)
        
class CaracSurcoBateas(models.Model):
    
    yacimiento = models.OneToOneField(Yacimiento, related_name='CaracSurcoBateas')
    
    largo = models.CharField('24.12. Largo (en cm)', blank = True, max_length=200)
    ancho = models.CharField('24.13. Ancho (en cm)', blank = True, max_length=200)
    diametro = models.CharField('24.13a. Diametro (en cm)',  blank = True, max_length=200)
    profundidad = models.CharField('24.13b. Profundidad (en cm)',  blank = True, max_length=200)
    abbr = 'cba'

    class Meta:
        verbose_name = '13.10. Bateas'
        verbose_name_plural = ''
        
    def __unicode__(self):
        return '' # '# ' + str(self.id)


class CaracSurcoPuntosAcopl (models.Model):

    yacimiento = models.OneToOneField(Yacimiento, related_name='CaracSurcoPuntosAcopl')
    esPunteado= models.BooleanField('24.14. Punteado')
    diametro = models.CharField('24.14a. Diametro (en cm)',  blank = True, max_length=200)
    profundidad = models.CharField('24.14b. Profundidad (en cm)',  blank = True, max_length=200)
    otros = models.CharField('24.14c. Otros',  blank = True, max_length=500)    
    
    abbr = 'cpa'
    
    class Meta:
        verbose_name = '13.11. Puntos Acoplados'
        verbose_name_plural = ''
        
    def __unicode__(self):
        return '' # '# ' + str(self.id)

class CaracSurcoCupulas (models.Model):
    
    yacimiento = models.OneToOneField(Yacimiento, related_name='CaracSurcoCupulas')
    largo = models.CharField('24.15. Largo (en cm)', blank = True, max_length=200)
    ancho = models.CharField('24.16. Ancho (en cm)', blank = True, max_length=200)
    diametro = models.CharField('24.17. Diámetro (en cm)', blank = True, max_length=200)
    profundidad = models.CharField('24.17a. Profundidad (en cm)',  blank = True, max_length=200)
    otros = models.CharField('24.17b. Otros',  blank = True, max_length=500)
    
    abbr = 'ccu'

    class Meta:
        verbose_name = '13.12. Cúpula'
        verbose_name_plural = ''
        
    def __unicode__(self):
        return '' # '# ' + str(self.id)

class CaracSurcoMortero (models.Model):

    yacimiento = models.OneToOneField(Yacimiento, related_name='CaracSurcoMortero')
    
    largo = models.CharField('24.9. Largo (en cm)', blank = True, max_length=200)
    ancho = models.CharField('24.10. Ancho (en cm)', blank = True, max_length=200)
    
    abbr = 'cmr'

    class Meta:
        verbose_name = '13.13. Mortero o Metate'
        verbose_name_plural = ''
        
    def __unicode__(self):
        return '' # '# ' + str(self.id)


class CaracDeLaPintura (models.Model):

    yacimiento = models.OneToOneField(Yacimiento, related_name='CaracDeLaPintura')

    esPinturaRupestre = models.BooleanField('13.2. Pintura Rupestre')
    esTecnicaDactilar = models.BooleanField('25.1.1. Técnica - Dactilar')
    esTecnicaFibra = models.BooleanField('25.1.2. Técnica - Fibra')
    otros = models.CharField('25.1.3. Técnica - Otros', blank = True, max_length=500)
    esLineaSencilla= models.BooleanField('25.2.1 Tipo de Línea - Sencilla')
    anchoDe = models.CharField('25.2.1.1 Ancho desde (en cm)', blank = True, max_length=200)
    anchoA = models.CharField('25.2.1.2 Ancho hasta (en cm)', blank = True, max_length=200)
    esLineaCompuesta= models.BooleanField('25.2.2 Tipo de Línea - Compuesta')
    anchoDeComp = models.CharField('25.2.2.1 Ancho desde (en cm)', blank = True, max_length=200)
    anchoAComp = models.CharField('25.2.2.2 Ancho hasta (en cm)', blank = True, max_length=200)
    esFiguraRellena = models.BooleanField('25.3. Figura Rellena')
    esImpresionDeManos = models.BooleanField('25.4. Impresión de Manos')
    esImpresionDeManosPositivo = models.BooleanField('25.4.1. Positivo')
    esImpresionDeManosNegativo = models.BooleanField('25.4.2. Negativo')
    tienesFigurasSuperpuestas = models.BooleanField('25.5. Figuras Superpuestas')
 
    abbr = 'pin'
    
    class Meta:
        verbose_name = '13.2. Pintura Rupestre'
        verbose_name_plural = '25. Características de la Pintura'
        
    def __unicode__(self):
        return '' # '# ' + str(self.id)

class Colores (models.Model):

    yacimiento = models.ForeignKey(Yacimiento, related_name='Colores')
    c = models.CharField('C', blank = True, max_length=200)
    m = models.CharField('M', blank = True, max_length=200)
    y = models.CharField('Y', blank = True, max_length=200)
    k = models.CharField('K', blank = True, max_length=200)

    abbr = 'col'
    
    class Meta:
        verbose_name = '25.6. Colores'
        verbose_name_plural = '25.6. Colores'
        
    def __unicode__(self):
        return '' # '# ' + str(self.id)
		
class DescColores (models.Model):

    yacimiento = models.OneToOneField(Yacimiento, related_name='ColoresPositiva')
    
    esPositiva = models.BooleanField('25.6.1 Positiva')
    posNegro = models.CharField('25.6.1.1 Negro', blank = True, max_length=200)
    posBlanco = models.CharField('25.6.1.2 Blanco', blank = True, max_length=200)
    posAmarillo = models.CharField('25.6.1.3 Amarillo', blank = True, max_length=200)
    posUnRojo = models.CharField('25.6.1.4 Un rojo', blank = True, max_length=200)
    posDosRojos = models.CharField('25.6.1.5 Dos rojos', blank = True, max_length=200)
    posTresRojos = models.CharField('25.6.1.6 Tres rojos', blank = True, max_length=200)
	
    esNegativa = models.BooleanField('25.6.2 Negativa')
    negNegro = models.CharField('25.6.2.1 Negro', blank = True, max_length=200)
    negBlanco = models.CharField('25.6.2.2 Blanco', blank = True, max_length=200)
    negAmarillo = models.CharField('25.6.2.3 Amarillo', blank = True, max_length=200)
    negUnRojo = models.CharField('25.6.2.4 Un rojo', blank = True, max_length=200)
    negDosRojos = models.CharField('25.6.2.5 Dos rojos', blank = True, max_length=200)
    negTresRojos = models.CharField('25.6.2.6 Tres rojos', blank = True, max_length=200)	
	
    colorBase = models.CharField('25.6.3 Color base (áreas interlineales)', blank = True, max_length=200)	
    abbr = 'dco'
    
    class Meta:
        verbose_name = '25.6. Colores'
        verbose_name_plural = ''
        
    def __unicode__(self):
        return '' # '# ' + str(self.id)
		
class CaracMonolitos(models.Model):

    yacimiento = models.OneToOneField(Yacimiento, related_name='CaracMonolitos')
    
    cantidad = models.IntegerField('26.1. Cantidad ', blank = True, null = True, )
    esPinturaRupestre = models.BooleanField('13.7.1.1 Con Grabados')
    cantidadConGrabados = models.IntegerField('26.2. Cantidad con Grabados', blank = True, null = True, )
    
    abbr = 'mon'

    class Meta:
        verbose_name = '13.7.1. Monolitos'
        verbose_name_plural = '26. Caracteristicas Monumentos Megalíticos'
        
    def __unicode__(self):
        return '' # '# ' + str(self.id)

class CaracMenhires(models.Model):
    
    yacimiento = models.OneToOneField(Yacimiento, related_name='CaracMehnires')
    
    sonPiedrasVerticales = models.BooleanField('26.0. Piedras Verticales')
    cantidadPiedrasVerticales = models.IntegerField('26.3. Cantidad', blank = True, null = True, )
    conPuntosAcoplados = models.BooleanField('13.7.2.1 Con Puntos Acoplados')
    cantidadConPuntosAcoplados = models.IntegerField('26.4. Cantidad', blank = True, null = True, )
    ConPetroglifo = models.BooleanField('13.7.2.2 Con Petroglifo')
    cantidadConPetroglifo = models.IntegerField('26.5. Cantidad', blank = True, null = True, )
    conPinturas = models.BooleanField('13.7.2.3 Con Pinturas')
    cantidadConPinturas = models.IntegerField('26.6. Cantidad', blank = True, null = True, )
    distanciamiento = models.IntegerField('26.7. Distanciamiento (en cm)', blank = True, null = True, )
    
    abbr = 'men'

    class Meta:
        verbose_name = '13.7.2. Menhires'
        verbose_name_plural = ''
        
    def __unicode__(self):
        return '' # '# ' + str(self.id)

class CaracDolmenArt(models.Model):
   
    yacimiento = models.OneToOneField(Yacimiento, related_name='CaracDolmenArt')
    
    ConPetroglifo = models.BooleanField('13.7.3.1. Con Petroglifo')
    cantidadConPetroglifo = models.IntegerField('26.8. Cantidad', blank = True, null = True, )
    conPinturas = models.BooleanField('13.7.3.2. Con Pinturas')
    cantidadConPinturas = models.IntegerField('26.9. Cantidad', blank = True, null = True, )
    
    abbr = 'dol'

    class Meta:
        verbose_name = '13.7.3. Dolmen'
        verbose_name_plural = ''
        
    def __unicode__(self):
        return '' # '# ' + str(self.id)

class NotasYacimiento(models.Model) :

    yacimiento = models.OneToOneField(Yacimiento, related_name='NotasYacimiento')
    notas = models.CharField('26.10. Notas', blank = True, max_length=500)

    abbr = 'dol'

    class Meta:
        verbose_name = '26.10 Notas'
        verbose_name_plural = '26.10 Notas'
        
    def __unicode__(self):
        return '' # '# ' + str(self.id)
