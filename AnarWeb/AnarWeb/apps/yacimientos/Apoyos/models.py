# -*- coding: utf-8 -*-

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ObjectDoesNotExist
from smart_selects.db_fields import ChainedForeignKey

from django.utils.safestring import mark_safe

from ..models import Yacimiento


class Bibliografia(models.Model):

    TIPO_MAPA = (
        (1, '1 - Radar'),
        (2, '2 - Satelital'),
    )

    """Representa la bibliografia de un yacimiento o una piedra """
	
    def __unicode__(self):
        return '' # '# ' + str(self.id)

class BibYacimiento(Bibliografia):

    yacimiento = models.ForeignKey(Yacimiento, related_name='BibYacimiento')
    
    esBibliografia = models.BooleanField('31.1 Bibliografía', default = True)
    codigo = models.CharField('31.1.1. Código', blank = True, max_length=200)
    titulo = models.CharField('31.1.2. Título', blank = True, max_length=200)
    autor  = models.CharField('31.1.3. Autor ', blank = True, max_length=200)
    ano = models.CharField('31.1.4. Año', blank = True, max_length=200)
    institucion  = models.CharField('31.1.5. Institución', blank = True, max_length=200)
    conDibujo = models.BooleanField('31.1.6. Con dibujo',)
    archivo = models.ImageField('31.1.6.1. Dibujo - Archivo', 
                                 upload_to='bibliografia_yac/%Y_%m', 
                                 null=True, 
                                 blank=True)
    
    esFotografia = models.BooleanField('31.1.7. Con fotografía')
    tieneFotografia = models.ImageField('31.1.7.1. Fotografía - Archivo', 
                                 upload_to='bibliografia_yac/%Y_%m', 
                                 null=True, 
                                 blank=True)
    escolor = models.BooleanField('31.1.7.1.1. Color')
    esBlancoYNegro = models.BooleanField('31.1.7.1.2. B/N')
    esDiapositiva = models.BooleanField('31.1.7.2. Diapositiva')
    esPapel = models.BooleanField('31.1.7.3. Papel')
    esDigital = models.BooleanField('31.1.7.4. Digital')
    esNegativo = models.BooleanField('31.1.7.5. Negativo')
    description = models.BooleanField('31.1.8. Con mapa')
    tieneMapa = models.ImageField('31.1.8.1. Mapa - Archivo', 
                                 upload_to='bibliografia_yac/%Y_%m', 
                                 null=True, 
                                 blank=True)
    tipoMapa = models.IntegerField('31.1.8.2. Tipo de mapa', choices = Bibliografia.TIPO_MAPA, blank = True,null = True)
	
    abbr = 'biy'
    
    class Meta:
        verbose_name = 'Bibliografía'
        verbose_name_plural = '31 Apoyos'

# Material audiovisual     

class MatAudioVisual (models.Model):

    #formato = models.CharField('1. Formato')
    #archivo = models.FileField('2. Material AV - Archivo', upload_to='audiovisual/%Y_%m', null=True, blank=True)
    
    def __unicode__(self):
        return '' # '# ' + str(self.id) 

class MatAVYacimiento(MatAudioVisual):

    yacimiento = models.ForeignKey(Yacimiento, related_name='MatAVYacimiento')
    ismatavy = models.BooleanField('31.2. Material audiovisual')
    format = models.CharField('31.2.1. Formato', max_length=200)
    archive = models.FileField('31.2.2. Material AV - Archivo', upload_to='audiovisual/%Y_%m', null=True, blank=True)
    
    abbr = 'avy'
    
    class Meta:
        verbose_name = 'Material audiovisual'
        verbose_name_plural = ''

# Videos 

class Video (models.Model):

    #anio = models.IntegerField('0. Año')
    #formato = models.CharField('1. Formato',)
    #titulo = models.CharField('2. Titulo')
    #autor = models.CharField('3. Autor')    
    #institucion = models.CharField('4. Institucion',)
    #numReferencia = models.IntegerField('5. Nro de referencia')
    #isFromAnar = models.BooleanField('6. ¿Es de ANAR?')
    #numCopia = models.IntegerField('6.1. Nro de copia')
    #archivo = models.FileField('7. Video - Archivo', upload_to='video/%Y_%m', null=True, blank=True)
    
    def __unicode__(self):
        return '' # '# ' + str(self.id) 
    
class VideoYacimiento (Video) :

    yacimiento = models.ForeignKey(Yacimiento, related_name='VideoYacimiento')
    isvidyac = models.BooleanField('31.3. Videos')
    anioy = models.IntegerField('31.3.0. Año')
    formatoy = models.CharField('31.3.1. Formato', max_length=200)
    tituloy = models.CharField('31.3.2. Titulo', max_length=200)
    autory = models.CharField('31.3.3. Autor', max_length=200)    
    instituciony = models.CharField('31.3.4. Institucion', max_length=200)
    numReferenciay = models.IntegerField('31.3.5. Nro de referencia')
    isFromAnary = models.BooleanField('31.3.6. ¿Es de ANAR?')
    numCopiay = models.IntegerField('31.3.6.1. Nro de copia')
    archivoy = models.FileField('31.3.7. Video - Archivo', upload_to='video/%Y_%m', null=True, blank=True)
    
    abbr = 'vdy'
    
    class Meta:
        verbose_name = 'Video'
        verbose_name_plural = ''

# Película

class Pelicula (Video):
    
    def __unicode__(self):
        return '' # '# ' + str(self.id) 

class PeliYacimiento (Pelicula):
    
    yacimiento = models.ForeignKey(Yacimiento, related_name='PeliYacimiento')
    
    abbr = 'ply'
    
    class Meta:
        verbose_name = 'Película'
        verbose_name_plural = '31.4. Películas'

# Página Web

class PaginaWeb (models.Model):
    
    direccionURL = models.URLField ('31.5.1. URL de página web')
    
    def __unicode__(self):
        return '' # '# ' + str(self.id) 

class PaginaWebYac (PaginaWeb):

    yacimiento = models.ForeignKey(Yacimiento, related_name='PaginaWebYac')
    
    abbr = 'pwy'
    
    class Meta:
        verbose_name = 'Página Web'
        verbose_name_plural = '31.5. Página Web'

# Multimedia

class Multimedia (models.Model):

    tecnica = models.CharField('31.6.1. Técnica', max_length=200 )
    archivo = models.FileField('31.6.2. Multimedia - Archivo', upload_to='multimedia/%Y_%m', null=True, blank=True)
    def __unicode__(self):
        return '' # '# ' + str(self.id) 

class MultimediaYac (Multimedia):

    yacimiento = models.ForeignKey(Yacimiento, related_name='MultimediaYac')
    
    abbr = 'mmy'
    
    class Meta:
        verbose_name = 'Multimedia'
        verbose_name_plural = '31.6. Multimedia'


# Obtencion de informacion

class ObtencionInfo (models.Model):

    prospeccion = models.BooleanField('32.1. Prospección sistemática')
    comunicacion = models.BooleanField('32.2. Comunicación personal')
    nombre = models.CharField('32.2.1. Nombre', max_length=200)
    direccion = models.CharField('32.2.2. Dirección', blank = True, max_length=200)
    telefono = models.CharField('32.2.3. Telefono/Fax',  blank = True, max_length=200)
    telefonoCel = models.CharField('32.2.4. Telefono celular',  blank = True, max_length=200)
    mail = models.EmailField('32.2.5. Correo electrónico', blank = True)
    paginaWeb = models.URLField('32.2.6. Página Web', blank = True)
    twitter = models.CharField('32.2.7. Twitter',  blank = True, max_length=200)
    nombreFacebook = models.CharField('32.2.8. Perfil Facebook',  blank = True, max_length=200)
    blog = models.URLField('32.2.9. Blog', blank = True)
    fecha = models.CharField('32.2.10. Fecha', blank = True, null= True, max_length=100)
    verificado = models.BooleanField('32.2.3. Verificado en el campo')

    def __unicode__(self):
        return '' # '# ' + str(self.id) 
    
class ObtInfoYac (ObtencionInfo):

    yacimiento = models.ForeignKey(Yacimiento, related_name='ObtInfoYac')
    
    abbr = 'oiy'
    
    class Meta:
        verbose_name = 'Información obtenida por'
        verbose_name_plural = '32. Información obtenida por'