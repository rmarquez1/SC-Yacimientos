# -*- coding: utf-8 -*-

from django.contrib import admin
from AnarWeb.apps.yacimientos import forms
from smart_selects.db_fields import ChainedForeignKey 

# Importar los modelos necesarios empezando por los de yacimiento
from .models import Yacimiento, LocalidadYacimiento, UsoActSuelo, TenenciaDeTierra, Indicaciones, Croquis, Plano , \
    Coordenadas , Datum , Altitud , FotografiaYac, TipoYacimiento, ManifestacionYacimiento, UbicacionYacimiento, OrientacionYacimiento , \
    TexturaSuelo , FloraYacimiento , FaunaYacimiento , HidrologiaYacimiento , TipoExposicionYac,\
    ConstitucionYacimiento , MaterialYacimiento, TecnicaParaGeoglifo  , TecnicaParaPintura  , TecnicaParaPetroglifo ,\
    TecnicaParaMicroPetro , TecnicaParaMonumentos , CaracSurcoPetroglifo , CaracSurcoAmoladores , CaracSurcoBateas,\
    CaracSurcoPuntosAcopl , CaracSurcoCupulas , CaracSurcoMortero , CaracDeLaPintura , Colores, DescColores, CaracMonolitos, \
    CaracMenhires, CaracDolmenArt, NotasYacimiento, EstadoConserYac, ConsiderTemp, \
	CausasDestruccionYac, IntensidadDestruccionYac, CronologiaTentativa, \
	ManifestacionesAsociadas, ManifestacionesLitica, ManifestacionesCeramica, ManifestacionesOseo, \
	ManifestacionesConcha, ManifestacionesCarbon, ManifestacionesMito, \
	ManifestacionesCementerio, ManifestacionesMonticulo, ManifestacionesOtros, \
    BibYacimiento, MatAVYacimiento, VideoYacimiento, PeliYacimiento , PaginaWebYac, \
    MultimediaYac , ObtInfoYac , OtrosValYac, ObservacionesYac, LlenadoYac, SupervisadoYac

########################################################################################
# Declaracion de modelos inlines para yacimiento
########################################################################################


class LocalidadYacInline(admin.StackedInline):
    model = LocalidadYacimiento
    form = forms.LocalidadYacimientoForm
    extra = 1
    max_num = 1
    suit_classes = 'suit-tab suit-tab-generales'
   
class UsoActSueloYacInline(admin.StackedInline):
    model = UsoActSuelo
    extra = 1
    max_num = 1
    suit_classes = 'suit-tab suit-tab-generales'

class TenenciaYacInline(admin.StackedInline):
    model = TenenciaDeTierra
    form = forms.TenenciaDeTierraForm
    extra = 1
    max_num = 1
    suit_classes = 'suit-tab suit-tab-generales'

class IndicacionesYacInline(admin.StackedInline):
    model = Indicaciones
    form = forms.IndicacionesForm
    extra = 1
    max_num = 1
    template = 'InlineTemplates/IndicacionesYacimiento.html'

class CroquisYacInline(admin.TabularInline):
    model = Croquis
    extra = 1
    suit_classes = 'suit-tab suit-tab-generales'

class PlanoYacInline(admin.StackedInline):
    model = Plano
    form = forms.PlanoForm
    extra = 1
    max_num = 1
    template = 'InlineTemplates/NumeroPlano.html'

class CoordenadasYacInline(admin.TabularInline):
    model = Coordenadas
    form = forms.CoordenadasForm
    extra = 1
    max_num = 1
    template = 'InlineTemplates/CoordenadasYac.html'
    suit_classes = 'suit-tab suit-tab-generales'

class DatumYacInline(admin.StackedInline):
    model = Datum
    extra = 1
    max_num = 1
    template = 'InlineTemplates/DatumGPS.html'
    suit_classes = 'suit-tab suit-tab-generales'

class AltitudYacInline(admin.StackedInline):
    model = Altitud
    form = forms.AltitudForm
    extra = 1
    max_num = 1
    template = 'InlineTemplates/AltitudYacimiento.html'

class FotoYacInline(admin.TabularInline):
    model = FotografiaYac
    extra = 1
    suit_classes = 'suit-tab suit-tab-generales'

class TipoYacimientoYacInline(admin.StackedInline):
    model = TipoYacimiento
    extra = 1
    max_num = 1
    template = 'InlineTemplates/TipoYacimiento.html'
    
class ManifestacionYacimientoInline(admin.StackedInline):
    model = ManifestacionYacimiento
    extra = 1
    max_num = 1
    template = 'InlineTemplates/ManifestacionYacimiento.html'
    
class UbicacionYacimientoInline(admin.StackedInline):
    model = UbicacionYacimiento
    extra = 1
    max_num = 1
    template = 'InlineTemplates/UbicacionYacimiento.html'

class OrientacionYacInline(admin.StackedInline):
    model = OrientacionYacimiento
    form = forms.OrientacionYacimientoForm
    extra = 1
    max_num = 1
    suit_classes = 'suit-tab suit-tab-manifestacion'

class TexturaYacInline(admin.StackedInline):
    model = TexturaSuelo
    form = forms.TexturaSueloForm
    extra = 1
    max_num = 1
    suit_classes = 'suit-tab suit-tab-generales'

class FloraYacInline(admin.StackedInline):
    model = FloraYacimiento
    form = forms.FloraYacimientoForm
    extra = 1
    max_num = 1
    suit_classes = 'suit-tab suit-tab-generales'

class FaunaYacInline(admin.StackedInline):
    model = FaunaYacimiento
    form = forms.FaunaYacimientoForm
    extra = 1
    max_num = 1
    suit_classes = 'suit-tab suit-tab-generales'

class HidrologiaYacInline(admin.StackedInline):
    model = HidrologiaYacimiento
    form = forms.HidrologiaYacimientoForm
    extra = 1
    max_num = 1
    suit_classes = 'suit-tab suit-tab-generales'

class TipoExposicionYacInline(admin.StackedInline):
    model = TipoExposicionYac
    form = forms.TipoExposicionYacForm
    extra = 1
    max_num = 1
    template = 'InlineTemplates/ExposicionYacimiento.html'

class ConstitucionYacInline(admin.StackedInline):
    model = ConstitucionYacimiento
    form = forms.ConstitucionYacimientoForm
    extra = 1
    max_num = 1
    suit_classes = 'suit-tab suit-tab-generales'

class MaterialYacInline(admin.StackedInline):
    model = MaterialYacimiento
    form = forms.MaterialYacimientoForm
    extra = 1
    max_num = 1
    template = 'InlineTemplates/MaterialYacimiento.html'

class TecnicaParaGeoglifoYacInline(admin.StackedInline):
    model = TecnicaParaGeoglifo
    form = forms.TecnicaParaGeoglifoForm
    extra = 1
    max_num = 1
    template = 'InlineTemplates/TecnicasYacimiento.html'

class TecnicaParaPinturaYacInline(admin.StackedInline):
    model = TecnicaParaPintura
    form = forms.TecnicaParaPinturaForm
    extra = 1
    max_num = 1
    template = 'InlineTemplates/stackedTecnicas.html'
    
class TecnicaParaPetroglifoYacInline(admin.StackedInline):
    model = TecnicaParaPetroglifo
    form = forms.TecnicaParaPetroglifoForm
    extra = 1
    max_num = 1
    template = 'InlineTemplates/stackedTecnicas.html'

class TecnicaParaMicroPetrYacInline(admin.StackedInline):
    model = TecnicaParaMicroPetro
    form = forms.TecnicaParaMicroPetroForm
    extra = 1
    max_num = 1
    template = 'InlineTemplates/stackedTecnicas.html'

class TecnicaParaMonumentosYacInline(admin.StackedInline):
    model = TecnicaParaMonumentos
    form = forms.TecnicaParaMonumentosForm
    extra = 1
    max_num = 1
    template = 'InlineTemplates/stackedTecnicas.html'

class CaracSurcoPetroglifoYacInline(admin.StackedInline):
    model = CaracSurcoPetroglifo
    form = forms.CaracSurcoPetroglifoForm
    extra = 1
    max_num = 1
    template = 'InlineTemplates/CaracteristicasSurcoYacimiento.html'

class CaracSurcoAmoladoresYacInline(admin.StackedInline):
    model = CaracSurcoAmoladores
    form = forms.CaracSurcoAmoladoresForm
    extra = 1
    max_num = 1
    template = 'InlineTemplates/stackedTecnicas.html'

class CaracSurcoBateasYacInline(admin.StackedInline):
    model = CaracSurcoBateas
    form = forms.CaracSurcoBateasForm
    extra = 1
    max_num = 1
    template = 'InlineTemplates/stackedTecnicas.html'

class CaracSurcoPuntosAcopladosYacInline(admin.StackedInline):
    model = CaracSurcoPuntosAcopl
    form = forms.CaracSurcoPuntosAcoplForm
    extra = 1
    max_num = 1
    template = 'InlineTemplates/stackedTecnicas.html'

class CaracSurcoCupulasYacInline(admin.StackedInline):
    model = CaracSurcoCupulas
    form = forms.CaracSurcoCupulasForm
    extra = 1
    max_num = 1
    template = 'InlineTemplates/stackedTecnicas.html'

class CaracSurcoMorteroYacInline(admin.StackedInline):
    model = CaracSurcoMortero
    form = forms.CaracSurcoMorteroForm
    extra = 1
    max_num = 1
    template = 'InlineTemplates/stackedTecnicas.html'

class CaracDeLaPinturaYacInline(admin.StackedInline):
    model = CaracDeLaPintura
    form = forms.CaracDeLaPinturaForm
    extra = 1
    max_num = 1
    template = 'InlineTemplates/CaracteristicasPinturaYacimiento.html'

class ColoresInline(admin.TabularInline):
    model = Colores  
    form = forms.ColoresForm	
    extra = 6
    template = 'InlineTemplates/ColoresYacimiento.html'    
    suit_classes = 'suit-tab suit-tab-tecnicas'	
	
class DescColoresInline(admin.StackedInline):
    model =DescColores  
    #form = forms.DescColoresForm	
    extra = 1
    max_num = 1    
    suit_classes = 'suit-tab suit-tab-tecnicas'	
	
class CaracMonolitosYacInline(admin.StackedInline):
    model = CaracMonolitos
    form = forms.CaracMonolitosForm
    extra = 1
    max_num = 1
    template = 'InlineTemplates/stackedTecnicas.html'

class CaracMenhiresYacInline(admin.StackedInline):
    model = CaracMenhires
    form = forms.CaracMenhiresForm
    extra = 1
    max_num = 1
    template = 'InlineTemplates/stackedTecnicas.html'

class CaracDolmenArtificialYacInline(admin.StackedInline):
    model = CaracDolmenArt
    form = forms.CaracDolmenArtForm
    extra = 1
    max_num = 1
    template = 'InlineTemplates/stackedTecnicas.html'

class NotasYacimientoInline(admin.StackedInline):
    model = NotasYacimiento
    form = forms.NotasYacimientoForm
    extra = 1
    max_num = 1
    suit_classes = 'suit-tab suit-tab-tecnicas'
    
class EstadoConservacionYacimientoYacInline(admin.StackedInline):
    model = EstadoConserYac
    form = forms.EstadoConserYacForm
    extra = 1
    max_num = 1
    template = 'InlineTemplates/EstadoConservacionYacimiento.html'

class CausasDestruccionYacInline(admin.StackedInline):
    model = CausasDestruccionYac
    form = forms.CausasDestruccionYacForm
    extra = 1
    max_num = 1
    suit_classes = 'suit-tab suit-tab-conservacion'

class IntensidadDestruccionYacInline(admin.StackedInline):
    model = IntensidadDestruccionYac
    form = forms.IntensidadDestruccionYacForm
    extra = 1
    max_num = 1
    suit_classes = 'suit-tab suit-tab-conservacion' 

class ConsideracionesTemporalidadYacInline(admin.StackedInline):
    model = ConsiderTemp
    form = forms.ConsiderTempForm
    extra = 1
    max_num = 1
    suit_classes = 'suit-tab suit-tab-conservacion'

class CronologiaTentativaYacInline(admin.StackedInline):
    model = CronologiaTentativa
    form = forms.CronologiaTentativaForm
    extra = 1
    suit_classes = 'suit-tab suit-tab-conservacion'

class ManifestacionesAsociadasYacInline(admin.StackedInline):
    model = ManifestacionesAsociadas
    form = forms.ManifestacionesAsociadasForm
    extra = 1
    max_num = 1
    template = 'InlineTemplates/ManifestacionYacimiento.html'

class ManifestacionesLiticaInline(admin.TabularInline):
    model = ManifestacionesLitica
    form = forms.ManifestacionesLiticaForm
    extra = 1
    max_num = 1
    suit_classes = 'suit-tab suit-tab-manifestaciones'

class ManifestacionesCeramicaInline(admin.TabularInline):
    model = ManifestacionesCeramica
    form = forms.ManifestacionesCeramicaForm
    extra = 1
    max_num = 1
    suit_classes = 'suit-tab suit-tab-manifestaciones'

class ManifestacionesOseoInline(admin.TabularInline):
    model = ManifestacionesOseo
    form = forms.ManifestacionesOseoForm
    extra = 1
    max_num = 1
    suit_classes = 'suit-tab suit-tab-manifestaciones'	

class ManifestacionesConchaInline(admin.TabularInline):
    model = ManifestacionesConcha
    form = forms.ManifestacionesConchaForm
    extra = 1
    max_num = 1
    suit_classes = 'suit-tab suit-tab-manifestaciones'	

class ManifestacionesCarbonInline(admin.TabularInline):
    model = ManifestacionesCarbon
    form = forms.ManifestacionesCarbonForm
    extra = 1
    max_num = 1
    suit_classes = 'suit-tab suit-tab-manifestaciones'		

class ManifestacionesMitoInline(admin.TabularInline):
    model = ManifestacionesMito
    form = forms.ManifestacionesMitoForm
    extra = 1
    max_num = 1
    suit_classes = 'suit-tab suit-tab-manifestaciones'	

class ManifestacionesCementerioInline(admin.TabularInline):
    model = ManifestacionesCementerio
    form = forms.ManifestacionesCementerioForm
    extra = 1
    max_num = 1
    suit_classes = 'suit-tab suit-tab-manifestaciones'		

class ManifestacionesMonticuloInline(admin.TabularInline):
    model = ManifestacionesMonticulo
    form = forms.ManifestacionesMonticuloForm
    extra = 1
    max_num = 1
    suit_classes = 'suit-tab suit-tab-manifestaciones'		

class ManifestacionesOtrosInline(admin.StackedInline):
    model = ManifestacionesOtros
    form = forms.ManifestacionesOtrosForm
    extra = 1
    max_num = 1
    suit_classes = 'suit-tab suit-tab-manifestaciones'		
	
class OtrosValoresSitioYacInline(admin.StackedInline):
    model = OtrosValYac
    form = forms.OtrosValForm
    extra = 1
    max_num = 1
    suit_classes = 'suit-tab suit-tab-manifestaciones'

class BibYacimientoInline(admin.StackedInline):
    model = BibYacimiento
    form = forms.BibliografiaForm
    extra = 1
    template = 'InlineTemplates/ApoyosYacimiento.html'

class MatAVYacimientoInline(admin.StackedInline):
    model = MatAVYacimiento
    form = forms.MatAudioVisualForm
    extra = 1
    suit_classes = 'suit-tab suit-tab-apoyos'

class VideoYacimientoInline(admin.StackedInline):
    model = VideoYacimiento
    form = forms.VideoForm
    extra = 1
    suit_classes = 'suit-tab suit-tab-apoyos'

class PeliYacimientoInline(admin.StackedInline):
    model = PeliYacimiento
    form = forms.VideoForm
    extra = 1
    suit_classes = 'suit-tab suit-tab-apoyos'

class PaginaWebYacInline(admin.TabularInline):
    model = PaginaWebYac
    form = forms.PaginaWebForm
    extra = 1
    suit_classes = 'suit-tab suit-tab-apoyos'    

class MultimediaYacInline(admin.StackedInline):
    model = MultimediaYac
    form = forms.MultimediaForm
    extra = 1
    suit_classes = 'suit-tab suit-tab-apoyos' 
   
class ObtenidaPorYacInline(admin.StackedInline):
    model = ObtInfoYac
    form = forms.ObtencionInfoForm
    extra = 1
    suit_classes = 'suit-tab suit-tab-apoyos'

class ObservacionYacInline(admin.StackedInline):
    model = ObservacionesYac
    form = forms.ObservacionesForm
    extra = 1
    max_num = 1
    suit_classes = 'suit-tab suit-tab-observaciones'

class LlenadaPorYacInline(admin.TabularInline):
    model = LlenadoYac
    extra = 1
    suit_classes = 'suit-tab suit-tab-observaciones'

class SupervisadaPorYacInline(admin.TabularInline):
    model = SupervisadoYac
    extra = 1
    suit_classes = 'suit-tab suit-tab-observaciones'

########################################################################################
# Declaracion y registro de administradores
########################################################################################
    
#Administrador del modelo de datos Yacimiento
#Usando los parametros de la extensión Suite, se mejora y organiza el admin
class YacimientoAdmin(admin.ModelAdmin):

    model = Yacimiento
    form = forms.YacimientoForm
    list_display = ('codigo','nombre', 'pais','estado', 'manifestaciones',)
    list_filter = ('codigo','pais', 'estado',)
    
    fieldsets = [
        ('Datos generales del Yacimiento', {
            'classes': ('suit-tab suit-tab-generales',),	
            'fields': ['codigo', 'pais', 'nombre', 'municipio','estado']
        }),                    
    ]
	
    def manifestaciones(self, object):
        return object.tipos_de_manifestaciones    
    manifestaciones.short_description = "13. Tipo de Manifestacion"


	
    inlines = [
        LocalidadYacInline,UsoActSueloYacInline,TenenciaYacInline,IndicacionesYacInline,CroquisYacInline,
        PlanoYacInline,CoordenadasYacInline,DatumYacInline,AltitudYacInline,FotoYacInline,
        TipoYacimientoYacInline,ManifestacionYacimientoInline, UbicacionYacimientoInline, OrientacionYacInline, TexturaYacInline,
        FloraYacInline,FaunaYacInline, HidrologiaYacInline, TipoExposicionYacInline, ConstitucionYacInline,
        MaterialYacInline,TecnicaParaGeoglifoYacInline,TecnicaParaPinturaYacInline,TecnicaParaPetroglifoYacInline,
        TecnicaParaMicroPetrYacInline,TecnicaParaMonumentosYacInline,CaracSurcoPetroglifoYacInline,
        CaracSurcoAmoladoresYacInline,CaracSurcoBateasYacInline, CaracSurcoPuntosAcopladosYacInline,
        CaracSurcoCupulasYacInline,CaracSurcoMorteroYacInline,CaracDeLaPinturaYacInline,
        ColoresInline, DescColoresInline,
		CaracMonolitosYacInline,CaracMenhiresYacInline, CaracDolmenArtificialYacInline, NotasYacimientoInline,
        EstadoConservacionYacimientoYacInline,CausasDestruccionYacInline, IntensidadDestruccionYacInline, 
		ConsideracionesTemporalidadYacInline,CronologiaTentativaYacInline,		
		ManifestacionesLiticaInline, ManifestacionesCeramicaInline, ManifestacionesOseoInline, 
		ManifestacionesConchaInline, ManifestacionesCarbonInline, ManifestacionesMitoInline, 
		ManifestacionesCementerioInline, ManifestacionesMonticuloInline, ManifestacionesOtrosInline,		
		OtrosValoresSitioYacInline, BibYacimientoInline,  MatAVYacimientoInline,
        VideoYacimientoInline, PeliYacimientoInline, PaginaWebYacInline, MultimediaYacInline, ObtenidaPorYacInline,
        ObservacionYacInline, LlenadaPorYacInline,SupervisadaPorYacInline
    ]
    suit_form_tabs = (('generales', 'Datos generales del Yacimiento'),
                      ('manifestacion', 'La Manifestación'),
                      ('tecnicas', 'Técnicas'),
                      ('conservacion', 'Conservación'),
                      ('manifestaciones', 'Manifestaciones Asociadas'),
                      ('apoyos', 'Apoyos'),
                      ('observaciones', 'Observaciones')                      
                      )

    suit_form_includes = (
        ('InlineTemplates/Glosario1.html', 'top', 'manifestaciones'),
    )
       
    class Media:
        css = {
            "all": ("apps/yacimientos/admin.css",)
        }
        js = ("apps/yacimientos/admin.js",)


admin.site.register(Yacimiento, YacimientoAdmin)