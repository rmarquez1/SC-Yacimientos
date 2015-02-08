# -*- coding: utf-8 -*-

from django.db import models
from AnarWeb.apps.yacimientos.models import  Yacimiento, CharField, Estado, Bibliografia,\
											 MatAudioVisual, Pelicula, Video, LlenadoPor, SupervisadoPor, \
											 PaginaWeb, Multimedia, ObtencionInfo, OtrosValores, Observaciones,\
                                             short_text
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ObjectDoesNotExist
from smart_selects.db_fields import ChainedForeignKey

from django.utils.safestring import mark_safe

# Create your models here.
########################################################################################
# Diagrama de roca
########################################################################################

class Roca(models.Model):

    """Representa la información de la ficha pa, recoge la información básica"""

    yacimiento = models.ForeignKey(Yacimiento, related_name='Yacimiento')
    
    codigo = models.CharField('0- Codigo de la roca', unique = True, max_length=20)#, primary_key=True)        
    nombre = CharField('1- Nombre de la roca', )
    
    def __unicode__(self):
        return short_text('Pa-' + self.codigo + '-' + self.nombre)
    
    abbr = 'pdr'

    class Meta:
        verbose_name = 'Roca'
        verbose_name_plural = 'Rocas'

class FotografiaRoca (models.Model):
    
    roca = models.ForeignKey(Roca, related_name='FotografiaRoca')
    aerea = models.BooleanField('1.2.1. Aerea')
    noEsAerea = models.BooleanField('1.2.2. No Aerea')
    satelital = models.BooleanField('1.2.3. Satelital')
    fecha = models.CharField('1.2.4. Fecha', blank = True, null= True, max_length=100)
    archivo = models.ImageField('1.2.5. Fotografía - Archivo', 
                                upload_to='roca/%Y_%m', 
                                null=True, 
                                blank=True)
    
    abbr = 'ftp'  

    class Meta:
        verbose_name = ''
        verbose_name_plural = '1.2. Fotografias'
		
    def __unicode__(self):
        return '' # '# ' + str(self.id)		

class Roca2(models.Model):
    """Continuacion de informacion de rocas """

    yacimiento = models.ForeignKey(Roca, related_name='Roca2')

    nombreFiguras = CharField('2- Nombre de las figuras', blank=True)    
    estado = models.ForeignKey(Estado, related_name='EstadoPied', verbose_name = '3- Estado', blank = True, null = True)
    numeroCaras = models.IntegerField('4- Numero de Caras')
    numeroCarasTrajabadas = models.IntegerField('5- Numero de caras trabajadas')

    abbr = 'pd2'  

    class Meta:
        verbose_name = ''
        verbose_name_plural = ''
        
    def __unicode__(self):
        return '' # '# ' + str(self.id) 


class DimensionRoca(models.Model):

    """Representa la información de las dimensiones de la roca"""

    roca = models.ForeignKey(Roca, related_name='DimensionRoca')
    
    dimensiones = CharField('6a. Número de cara trabajada')
    alto =  CharField('7.1. Alto ' , blank = True)
    largo = CharField('7.2. Largo ', blank = True)
    ancho = CharField('7.3. Ancho ', blank = True)
                                        
    abbr = 'dip'
    
    def __unicode__(self):
        return '' # '# ' + str(self.id)
		
    class Meta:
        verbose_name = ''
        verbose_name_plural = '7. Dimensiones de la roca'

class CaraTrabajada(models.Model):

    """Representa la información de la ficha pa, referente a las caras trabajadas """
    
    ORIENTACION_CARA_TRABAJADA = (
        (0, '0 - Tope'),
        (1, '1 - Norte'),
        (2, '2 - Noreste'),
        (3, '3 - Este'),
        (4, '4 - Sureste'),
        (5, '5 - Sur'),
        (6, '6 - Suroeste'),
        (7, '7 - Oeste'),
        (8, '8 - Noroeste'),
        (9, '9 - Piso o plano inclinado'),
		(10, 'n - Desconocida')
    )

    AYUDA_OCT='En caso de no conocerse la orientación cardinal úsese la letra "n" (no conocido) en lugar del número respectivo. Para más de una cara trabajada sin orientación cardinal conocida, úsese n1, n2, n3 y así sucesivamente según el número de caras trabajadas, por roca. Usese estas mismas denominaciones en todos los casos en que se pida el número de la cara trabajada. (Punto 6, 7, 9 y 10).'

    AYUDA_NCT='En rocas al aire libre se contarán únicamente las caras factibles de trabajar; no se cuenta la cara apoyada sobre el suelo. En cuevas se cuentan el piso, el techo y las paredes internas. En abrigos se pueden agregar paredes externas factibles de trabajar '
	
    roca = models.ForeignKey(Roca, related_name='CaraTrabajada')
    numero =  CharField('6a. Número de cara trabajada',help_text=AYUDA_NCT )
    orientacion = models.IntegerField('6b. Orientación de la cara', choices = ORIENTACION_CARA_TRABAJADA, help_text= AYUDA_OCT)
    
    abbr = 'cat'

    def __unicode__(self):
        return '' # '# ' + str(self.id)
	
    class Meta:
        verbose_name = ''
        verbose_name_plural = '6. Caras trabajadas'

class UbicacionCaras(models.Model):

    """Representa la información de la ficha pa, referente a la ubicacion
    de las  caras trabajadas """

    LUMINOSIDAD = (
        (0, 'No tiene'),
        (1, 'Fótico'),
        (2, 'Escótico'),
    )

    roca = models.OneToOneField(Roca, related_name='UbicacionCaras')
    
    todaLaCaverna = models.BooleanField('8.1. Toda la caverna')
    areasEspecificas = models.BooleanField('8.2. Áreas específicas')
    salaPrincipal = models.BooleanField('8.2.1. Sala principal')
    otraSala = models.BooleanField('8.2.2. Otra sala')
    lagoInterior = models.BooleanField('8.2.3. Lago interior')
    claraboya = models.BooleanField('8.2.4. Claraboya')

    principalMouth = CharField('8.3. Distancia Boca Principal',blank=True, null=True)
    luminosity = models.IntegerField('8.3.1. Luminosidad', choices = LUMINOSIDAD, blank=True, null=True)
    heights = CharField('8.3.2. Altura', blank=True, null=True)   
    requiereAndamiaje = models.BooleanField('8.3.2.1. ¿Requiere andamiaje?')
    
    abbr = 'uca'
	
    def __unicode__(self):
        return '' # '# ' + str(self.id)    
	
    class Meta:
        verbose_name = ''
        verbose_name_plural = '8. Ubicación caras trabajadas (Cuevas/Abrigos)'
        

class FigurasPorTipo(models.Model):

    """Representa la información de la ficha pa, referente a los conjuntos de
    figuras por tipo presentes en cada cara"""

    TIPO_FIGURA = (
        (1, '9.1 - Antropomorfas'),
        (2, '9.2 - Zoomorfas'),
        (3, '9.3 - Geométricas'),
        (4, '9.4 - Puntos Acoplados'),
        (5, '9.5 - Cupulas'),
        (6, '9.6 - Zoo-antropomorfas'),
        (7, '9.7 - Antropo-geométricas'),
        (8, '9.8 - Zoo-geométricas'),
        (9, '9.9 - Amoladores'),
        (10, '9.10 - Bateas'),
    )

    AYUDA_CID= 'Utilícese la letra "i" (incompleto) delante del número, para los casos en que la cantidad de figuras, sea mayor que la expuesta, pero no se pueda cuantificar con exactitud, que sea mayor por la altura de los grabados, por efectos de erosión u otros. \n Por ejemplo, en la cara 4 de una roca hay más de 25 puntos, sin poderse cuantificar con exactitud esa cifra. Se coloca entonces: i-25.\nPara aquellos casos en que se desconozcan las cantidades totalmente, se usará "i" en lugar de números.'

   
    roca = models.ForeignKey(Roca, related_name='FigurasPorTipo')    
    numero =  CharField( '6.a. Número de cara trabajada') 
    tipoFigura = models.IntegerField('9. Figuras',choices = TIPO_FIGURA)	
    cantidad = CharField('9.a. Cantidad', blank=True)  
    esCantidadInexacta = models.CharField('9.b. Cantidad Inexacta O Desconocida', max_length=10, help_text= AYUDA_CID, blank=True)	
    descripcion = CharField('9.c. Descripcion', blank=True)
    abbr = 'fpt'    
    
    def __unicode__(self):
        return '' # '# ' + str(self.id)
		
    class Meta:
        verbose_name = ''
        verbose_name_plural = '9. Figuras'

class EsquemaPorCara(models.Model):

    """Representa la información de la ficha pa, referente al esquema
    de la cara de la roca"""

    roca = models.ForeignKey(Roca, related_name='EsquemaPorCara')    
    numero =  CharField( '6.a. Número de cara trabajada ')  
    textoCara = CharField('10.1. Cara') 
    posicion = CharField('10.2. Posicion de las figuras en la cara', ) 
    
    def __unicode__(self):
        return '' # '# ' + str(self.id)
		
    abbr = 'epc'

    class Meta:
        verbose_name = 'Esquema por cara'
        verbose_name_plural = '10. Esquemas por caras'

class ConexionFiguras(models.Model):

    """Representa la información de la ficha pa, referente a la conexion
    de las figuras en la roca"""
    CONEXION_FIGURAS = (
        (1, '1 - Presencia de una sola figura'),
        (2, '2 - Menos del 10% interconectadas'),
        (3, '3 - 50% interconectadas'),
        (4, '4 - Mas del 80% interconectadas'),
    )    
    roca = models.OneToOneField(Roca, related_name='ConexionFiguras')    
    conexionFiguras = models.IntegerField('11. Conexion de figuras', choices = CONEXION_FIGURAS)
    
    def __unicode__(self):
        return '' # '# ' + str(self.id)
		
    abbr = 'cnx'
    
    class Meta:
        verbose_name = ''
        verbose_name_plural = ''

class Manifestaciones(models.Model):

    """Representa la información de la ficha pa, indicando el tipo de manifestacion"""

    roca = models.ForeignKey(Roca, related_name='Manifestaciones')
    
    tienePetroglifos = models.BooleanField('1.2.1. Petroglifos', blank=True)
    tieneRupestres = models.BooleanField('1.2.2. Pintura Rupestre', blank=True)
    tieneAmoladore = models.BooleanField('1.2.3. Amoladores', blank=True)
    tienePuntosAc = models.BooleanField('1.2.4. Puntos Acoplados', blank=True)
    tieneCupula = models.BooleanField('1.2.5. Cupulas', blank=True)
    hasMitos = CharField('1.2.6. Mitos', blank=True) 
    hasOtros = CharField('1.2.7. Otros', blank=True)
    
    def __unicode__(self):
        return '' # '# ' + str(self.id)
	
    abbr = 'man'
    
    class Meta:
        verbose_name = ''
        verbose_name_plural = '1.2 Manifestaciones Asociadas'

########################################################################################
# Tipos bases de multimedia
# Las clases que heredan de ella y son especificas a roca o yacimiento
########################################################################################

# Tratamiento fotografico

class TratFoto(models.Model):

    """Representa el tratamiento dado a las fotografias recopiladas"""
    
    limpiezaCon = CharField('12.1. Limpieza con', blank=True)
    rellenoSurcos = CharField('12.2. Relleno de surcos con', blank=True)
    tratamientoDigital = CharField('12.3. Tratamiento digital', blank=True)
    programaVersion = CharField('12.4. Programa/versión', blank=True)
    otrosTratamientos = CharField('12.5. Otros', blank=True)

    def __unicode__(self):
        return '' # '# ' + str(self.id)
		
class TratFotoRoca (TratFoto):

    """Representa el tratamiento dado a las fotografias recopiladas
    de las rocas"""

    roca = models.OneToOneField(Roca, related_name='TratFotoRoca')
    
    abbr = 'tpp'
    
    class Meta:
        verbose_name = ''
        verbose_name_plural = '12. Tratamiento para fotografías'

# Fotografia

class Foto (models.Model):

    """Representa la información de la fotografia"""
    
    TIPO_FOTOGRAFIA = (
        (1, 'Aerea'),
        (2, 'No aerea'),
        (3, 'Satelital'),
    )

    esfoto = models.BooleanField('13.1 Fotográfico')
    negativo =  CharField('13.1.0. Negativo', blank=True)
    tipoFotoA  = models.BooleanField('13.1.0.1. Aerea')
    tipoFotoNA = models.BooleanField('13.1.0.2. No Aerea')
    tipoFotoS  = models.BooleanField('13.1.0.3. Satelital')
    fecha = models.CharField('13.1.1. Fecha', blank = True, null= True, max_length=100)
    fotografo  = CharField('13.1.2. Fotógrafo', blank = True)
    institucion  = CharField('13.1.3. Institucion ', blank = True)
    numReferencia = CharField('13.1.4. Nro de referencia', blank = True)
    numRollo = CharField('13.1.5. Nro de rollo', blank = True)
    numFoto = CharField('13.1.6. Nro de foto', blank = True)
    numMarcaNegativo = CharField('13.1.7. Nro marca en negativo', blank = True)
    esDeAnar = models.BooleanField('13.1.8. ¿Es de Anar?')
    numCopiaAnarFoto = models.IntegerField('13.1.8.1. Num Copia ANAR', blank=True, null=True)

    def __unicode__(self):
        return '' # '# ' + str(self.id)
	

class FotoRoca (Foto):

    roca = models.ForeignKey(Roca, related_name='FotoRoca')
    
    abbr = 'fop'
    
    class Meta:
        verbose_name =  ''
        verbose_name_plural = '13 Apoyos'

# Representación gráfica de la roca

class RepGrafRoca (models.Model):

    """Representa la información de la ficha pa, agrupa los distintos tipos
    de reproducciones gráficas a escala natural y reducida"""

    roca = models.ForeignKey(Roca, related_name='RepGrafRoca')
	
    def __unicode__(self):
        return '' # '# ' + str(self.id)
    
    abbr = 'rgp'

class EscNatRoca(RepGrafRoca):

    TIPO_REPRODUCCION_NATURAL = (
        (1, '1 - Plana'),
        (2, '2 - Frotage'),
        (3, '3 - Calco'),
        (4, '4 - Tridimensional'),
        (5, '5 - Resina'),
        (6, '6 - Yeso'),
        (7, '7 - Papel de arroz'),
    )
    esEscNatRoca = models.BooleanField('13.2.1. Reproducción gráfica escala natural')
    tipoReproduccione = models.IntegerField('13.2.1.1. Reproducción gráfica', choices = TIPO_REPRODUCCION_NATURAL, blank = True)
    numPiezasP = models.IntegerField('13.2.1.2. Número de piezas', blank = True)
    institutoP  = CharField('13.2.1.3. Institución ', blank = True )
    personaP  = CharField('13.2.1.4. Persona ', blank = True )

    abbr = 'enp'

    class Meta:
        verbose_name = ''
        verbose_name_plural = ''
    
class EscRedRoca(RepGrafRoca):

    """Representa la información de la ficha pa, de reproducciones gráficas
    a escala reducida"""
        
    TIPO_REPRODUCCION_REDUCIDA = (
        (1, '1 - Dibujo'),
        (2, '2 - Matriz'),
    )
    esEscNatRoca = models.BooleanField('13.3.1. Reproducción gráfica escala reducida')
    tipoReproduccion = models.IntegerField('13.3.1.1. Reproducción gráfica', choices = TIPO_REPRODUCCION_REDUCIDA, blank = True)
    numPiezasP = models.IntegerField('13.3.1.2. Número de piezas', blank = True)
    institutoP  = CharField('13.3.1.3. Institución ', blank = True )
    personaP  = CharField('13.3.1.4. Persona ', blank = True )
    
    abbr = 'erp'

    class Meta:
        verbose_name = ''
        verbose_name_plural = ''

# Bibliografia

class BibRoca(Bibliografia):

    roca = models.ForeignKey(Roca, related_name='BibRoca')
    esbilbio = models.BooleanField('13.4. Bibliografía')
    tienePDF = models.BooleanField('13.4.0. PDF')
    pdfarchivo = models.FileField('13.4.0.1. Archivo - PDF',
                            upload_to='bibliografia_pie/%Y_%m', 
                            null=True, 
                            blank=True)
    pdfarchivo1 = models.FileField('13.4.0.2. Archivo - PDF',
                            upload_to='bibliografia_pie/%Y_%m', 
                            null=True, 
                            blank=True)
    pdfarchivo2 = models.FileField('13.4.0.3. Archivo - PDF',
                            upload_to='bibliografia_pie/%Y_%m', 
                            null=True, 
                            blank=True)
    tieneWord = models.BooleanField('13.4.0. Word')
    wordarchivo = models.FileField('13.4.0.1. Archivo - Word',
                            upload_to='bibliografia_pie/%Y_%m', 
                            null=True, 
                            blank=True)
    wordarchivo1 = models.FileField('13.4.0.2. Archivo - Word',
                            upload_to='bibliografia_pie/%Y_%m', 
                            null=True, 
                            blank=True)        
    codigo = CharField('13.4.1. Código', blank = True)
    titulo = CharField('13.4.2. Título', blank = True)
    autor  = CharField('13.4.3. Autor ', blank = True)
    ano = CharField('13.4.4. Fecha', blank = True)	
    institucion  = CharField('13.4.5. Institución', blank = True)
    conDibujo = models.BooleanField('13.4.6. Con dibujo')
    archivo = models.FileField('13.4.6.1. Dibujo - Archivo', 
                                upload_to='bibliografia_pie/%Y_%m', 
                                null=True, 
                                blank=True)
    archivo1 = models.FileField('13.4.6.2. Dibujo - Archivo', 
                                upload_to='bibliografia_pie/%Y_%m', 
                                null=True, 
                                blank=True)
    archivo2 = models.FileField('13.4.6.3. Dibujo - Archivo', 
                                upload_to='bibliografia_pie/%Y_%m', 
                                null=True, 
                                blank=True)
    archivo3 = models.FileField('13.4.6.4. Dibujo - Archivo', 
                                upload_to='bibliografia_pie/%Y_%m', 
                                null=True, 
                                blank=True)
    archivo4 = models.FileField('13.4.6.5. Dibujo - Archivo', 
                                upload_to='bibliografia_pie/%Y_%m', 
                                null=True, 
                                blank=True)
    esFotografia = models.BooleanField('13.4.7. Con fotografía')
    tieneFotografia = models.FileField('13.4.7.0.0. Fotografía - Archivo', 
                                 upload_to='bibliografia_pie/%Y_%m', 
                                 null=True, 
                                 blank=True)
    tieneFotografia1 = models.FileField('13.4.7.0.1. Fotografía - Archivo', 
                                 upload_to='bibliografia_pie/%Y_%m', 
                                 null=True, 
                                 blank=True)
    tieneFotografia2 = models.FileField('13.4.7.0.2. Fotografía - Archivo', 
                                 upload_to='bibliografia_pie/%Y_%m', 
                                 null=True, 
                                 blank=True)
    tieneFotografia3 = models.FileField('13.4.7.0.3. Fotografía - Archivo', 
                                 upload_to='bibliografia_pie/%Y_%m', 
                                 null=True, 
                                 blank=True)
    tieneFotografia4 = models.FileField('13.4.7.0.4. Fotografía - Archivo', 
                                 upload_to='bibliografia_pie/%Y_%m', 
                                 null=True, 
                                 blank=True)
    escolor = models.BooleanField('13.4.7.1. Color')
    esBlancoYNegro = models.BooleanField('13.4.7.2. B/N')
    esDiapositiva = models.BooleanField('13.4.7.3. Diapositiva')
    esPapel = models.BooleanField('13.4.7.4. Papel')
    esDigital = models.BooleanField('13.4.7.5. Digital')
    esNegativo = models.BooleanField('13.4.7.6. Negativo')
    description  = models.BooleanField('13.4.8. Con mapa ')
    tieneMapa = models.FileField('13.4.8.0.0. Mapa - Archivo', 
                                 upload_to='bibliografia_pie/%Y_%m', 
                                 null=True, 
                                 blank=True)
    tieneMapa1 = models.FileField('13.4.8.0.1. Mapa - Archivo', 
                                 upload_to='bibliografia_pie/%Y_%m', 
                                 null=True, 
                                 blank=True)
    tieneMapa2 = models.FileField('13.4.8.0.2. Mapa - Archivo', 
                                 upload_to='bibliografia_pie/%Y_%m', 
                                 null=True, 
                                 blank=True)
    tieneMapa3 = models.FileField('13.4.8.0.3. Mapa - Archivo', 
                                 upload_to='bibliografia_pie/%Y_%m', 
                                 null=True, 
                                 blank=True)
    tieneMapa4 = models.FileField('13.4.8.0.4. Mapa - Archivo', 
                                 upload_to='bibliografia_pie/%Y_%m', 
                                 null=True, 
                                 blank=True)
    tipoMapa = models.IntegerField('13.4.8.1. Tipo de mapa', choices = Bibliografia.TIPO_MAPA,blank = True,null = True)
	
    abbr = 'bip'
    
    class Meta:
        verbose_name = ''
        verbose_name_plural = ''

class MatAVRoca(MatAudioVisual):

    roca = models.ForeignKey(Roca, related_name='MatAVRoca')
    ismatavy = models.BooleanField('13.5. Material audiovisual')
    format = CharField('13.5.1. Formato', blank = True)
    archive = models.FileField('13.5.2. Material AV - Archivo', upload_to='audiovisual/%Y_%m', null=True, blank=True)
    
    abbr = 'avp'

    class Meta:
        verbose_name = 'Material audiovisual'
        verbose_name_plural = ''

# Video

class VideoRoca (Video) :

    roca = models.ForeignKey(Roca, related_name='VideoRoca')
    isvidyac = models.BooleanField('13.6. Videos')
    anioy = models.IntegerField('13.6.0. Año', blank = True)
    formatoy = CharField('13.6.1. Formato', blank = True)
    tituloy = CharField('13.6.2. Titulo', blank = True)
    autory = CharField('13.6.3. Autor', blank = True)    
    instituciony = CharField('13.6.4. Institucion', blank = True)
    numReferenciay = models.IntegerField('13.6.5. Nro de referencia', blank = True)
    isFromAnary = models.BooleanField('13.6.6. ¿Es de ANAR?')
    numCopiaRoca = models.IntegerField('13.6.6.1. Nro de copia', blank=True, null=True)
    archivoy = models.FileField('13.6.7. Video - Archivo', upload_to='video/%Y_%m', null=True, blank=True)

    abbr = 'vdp'
    
    
    class Meta:
        verbose_name = 'Video'
        verbose_name_plural = ''

# Película

class PeliculaRoca (Pelicula):

    roca = models.ForeignKey(Roca, related_name='PeliculaRoca')
    isvidyac = models.BooleanField('13.7. Películas')
    anioy = models.IntegerField('13.7.0. Año', blank = True)
    formatoy = CharField('13.7.1. Formato', blank = True)
    tituloy = CharField('13.7.2. Titulo', blank = True)
    autory = CharField('13.7.3. Autor', blank = True)    
    instituciony = CharField('13.7.4. Institucion', blank = True)
    numReferenciay = models.IntegerField('13.7.5. Nro de referencia', blank = True)
    isFromAnary = models.BooleanField('13.7.6. ¿Es de ANAR?')
    numCopiaRoca = models.IntegerField('13.7.6.1. Nro de copia', blank=True, null=True)
    archivoy = models.FileField('13.7.7. Video - Archivo', upload_to='video/%Y_%m', null=True, blank=True)
    
    abbr = 'plp'
    
    class Meta:
        verbose_name = 'Película'
        verbose_name_plural = ''

# Página Web

class PaginaWebRoca (PaginaWeb):

    roca = models.ForeignKey(Roca, related_name='PaginaWebRoca')
    tieneWb = models.BooleanField('13.8. Página Web')
    direccionURLP = models.URLField ('13.8.1. URL de página web')
    
    abbr = 'pwp'
    
    class Meta:
        verbose_name = 'Página Web'
        verbose_name_plural = ''

# Multimedia

class MultimediaRoca (Multimedia):

    roca = models.ForeignKey(Roca, related_name='MultimediaRoca')
    ismult = models.BooleanField('13.9. Multimedia')
    tecnicaP = CharField('31.6.1. Técnica', blank = True )
    archivoP = models.FileField('31.6.2. Multimedia - Archivo', upload_to='multimedia/%Y_%m', null=True, blank=True)
    abbr = 'mmp'
    
    class Meta:
        verbose_name = 'Multimedia'
        verbose_name_plural = ''

# Obtencion de informacion

class ObtInfoRoca (ObtencionInfo):

    roca = models.ForeignKey(Roca, related_name='ObtInfoRoca')
    isinfo = models.BooleanField('14. Información obtenida por')
    prospeccionP = models.BooleanField('14.1. Prospección sistemática')
    comunicacionP = models.BooleanField('14.2. Comunicación personal')
    nombreP = CharField('14.2.1. Nombre', blank=True)
    direccionP = CharField('14.2.2. Dirección', blank = True)
    telefonoP = CharField('14.2.3. Telefono/Fax',  blank = True)
    telefonoCelP = CharField('14.2.4. Telefono celular',  blank = True)
    mailP = models.EmailField('14.2.5. Correo electrónico', blank = True)
    paginaWebP = models.URLField('14.2.6. Página Web', blank = True)
    twitterP = CharField('14.2.7. Twitter',  blank = True)
    nombreFacebookP = CharField('14.2.8. Perfil Facebook',  blank = True)
    blogP = models.URLField('14.2.9. Blog', blank = True)
    fechaP = models.CharField('14.2.10. Fecha', blank = True, null= True, max_length=100)
    verificadoP = models.BooleanField('14.2.3. Verificado en el campo')
    
    abbr = 'oip'

    class Meta:
        verbose_name = 'Información obtenida por'
        verbose_name_plural = ''
    
# Otros valores

class OtrosValRoca(OtrosValores):

    roca = models.ForeignKey(Roca, related_name='OtrosValRoca')
    texto = CharField('15.1. Otros valores de la roca', blank = True)
    abbr = 'ovp'
    
    class Meta:
        verbose_name = ''
        verbose_name_plural = '15. Otros valores de la Roca'

# Observaciones

class ObservacRoca(Observaciones):

    roca = models.ForeignKey(Roca, related_name='ObservacRoca')
    textoR = CharField('16.1. Observaciones',)
    
    abbr = 'opi'
    
    class Meta:
        verbose_name = ''
        verbose_name_plural = '16. Observaciones'

# Llenado de la ficha
    
class LlenadoRoca(LlenadoPor):    

    roca = models.ForeignKey(Roca, related_name='LlenadoRoca')
    nombreR = CharField('17.1. Llenada por: ', blank = True)
    fechaR = models.CharField('17.2. Fecha', blank = True, null= True, max_length=100)
    
    abbr = 'ypp'
    
    class Meta:
        verbose_name = ''
        verbose_name_plural = '17. Ficha llenada por'

# Supervision de la ficha

class SupervisadoRoca(SupervisadoPor):
    
    roca = models.ForeignKey(Roca, related_name='SupervisadoRoca')
    nombreR = CharField('18.1. Supervisada por: ', blank = True)
    fechaR = models.CharField('18.2. Fecha', blank = True, null= True, max_length=100)
    
    abbr = 'spp'    

    class Meta:
        verbose_name = ''
        verbose_name_plural = '18. Ficha Supervisada Por'