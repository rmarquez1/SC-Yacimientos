# -*- coding: utf-8 -*-

from django.contrib import admin
from AnarWeb.apps.yacimientos import forms as YacForms
from AnarWeb.apps.Rocas import forms
from smart_selects.db_fields import ChainedForeignKey 

# Importar los modelos necesarios empezando por los de roca
from .models import \
    Roca, Roca2, FotografiaRoca, DimensionRoca, CaraTrabajada, UbicacionCaras, FigurasPorTipo, EsquemaPorCara, ConexionFiguras, \
    Manifestaciones, TratFotoRoca, TratFotoRoca, FotoRoca, EscNatRoca, EscRedRoca, \
    BibRoca, MatAVRoca, VideoRoca, PeliculaRoca, PaginaWebRoca, MultimediaRoca, \
    ObtInfoRoca, OtrosValRoca, ObservacRoca, LlenadoRoca, SupervisadoRoca

########################################################################################
# Declaracion de modelos inlines para roca
########################################################################################

class Roca2Inline(admin.StackedInline):
    extra = 1
    max_num = 1
    model = Roca2
    template = 'InlineTemplates/ContinuacionRoca.html'

class FotografiaRocaInline(admin.TabularInline):
    extra = 1 
    model =  FotografiaRoca 
    suit_classes = 'suit-tab suit-tab-generales'

class DimensionRocaInline(admin.TabularInline):
    extra = 4
    model =  DimensionRoca
    form = forms.DimensionRocaForm
    template = 'InlineTemplates/DimensionesRoca.html'

class ManifestacionesInline(admin.StackedInline):
    extra = 1
    max_num = 1
    model =  Manifestaciones
    form = forms.ManifestacionesAsociadasForm
    template = 'InlineTemplates/ManifestacionesRoca.html'

class CaraTrabajadaInline(admin.TabularInline):
    extra = 6
    model = CaraTrabajada
    form = forms.CaraTrabajadaForm
    template = 'InlineTemplates/CarasTrabajadasRoca.html'

class UbicacionCarasInline(admin.StackedInline):
    extra = 1
    max_num = 1
    model = UbicacionCaras
    form = forms.UbicacionCarasForm
    template = 'InlineTemplates/UbicacionCaras.html'

class FigurasPorTipoInline(admin.TabularInline):
    extra = 10
    max_num = 60  
    model =  FigurasPorTipo
    form = forms.FigurasPorTipoForm
    template = 'InlineTemplates/FigurasRoca.html'
	
class EsquemaPorCaraInline(admin.TabularInline):
    extra = 6
    max_num = 6
    model =  EsquemaPorCara
    template = 'InlineTemplates/EsquemasPorCaras.html'
	
class ConexionFigurasInline(admin.StackedInline):
    extra = 1
    max_num = 1
    model =  ConexionFiguras
    template = 'InlineTemplates/ConexionFiguras.html'

class TratFotoInline(admin.StackedInline):
    extra = 1
    model =  TratFotoRoca
    form = forms.TratFotoRocaForm
    template = 'InlineTemplates/TratamientoFoto.html'

class OtrosValRocaInline(admin.StackedInline):
    model = OtrosValRoca
    form = YacForms.OtrosValForm
    extra = 1
    max_num = 1
    template = 'InlineTemplates/OtrosValoresRoca.html'    
	
class FotoDigRocaInline(admin.StackedInline):
    extra = 1
    model =  FotoRoca
    form = YacForms.FotoForm
    template = 'InlineTemplates/ApoyosRoca.html'

class EscalaNatRocaInline(admin.StackedInline):
    extra = 1
    model =  EscNatRoca
    form = forms.RepGrafRocaForm
    template = 'InlineTemplates/stackedApoyos.html'

class EscalaRedRocaInline(admin.StackedInline):
    model =  EscRedRoca
    form = forms.RepGrafRocaForm
    extra = 1
    template = 'InlineTemplates/stackedApoyos.html'

class BibRocaInline(admin.StackedInline):
    extra = 1
    model =  BibRoca
    form = YacForms.BibliografiaForm
    template = 'InlineTemplates/stackedApoyos.html'


class MatAudioVisualInline(admin.StackedInline):
    extra = 1
    model =  MatAVRoca
    form = YacForms.MatAudioVisualForm
    suit_classes = 'suit-tab suit-tab-apoyos'

class VideoRocaInline(admin.StackedInline):
    extra = 1
    model =  VideoRoca
    form = YacForms.VideoForm
    suit_classes = 'suit-tab suit-tab-apoyos'

class PeliculaRocaInline(admin.StackedInline):
    extra = 1
    model =  PeliculaRoca
    form = YacForms.VideoForm
    suit_classes = 'suit-tab suit-tab-apoyos'

class PaginaWebRocaInline(admin.TabularInline):
    extra = 1 
    model =  PaginaWebRoca
    form = YacForms.PaginaWebForm
    suit_classes = 'suit-tab suit-tab-apoyos'

class MultimediaRocaInline(admin.StackedInline):
    extra = 1
    model =  MultimediaRoca
    form = YacForms.MultimediaForm
    suit_classes = 'suit-tab suit-tab-apoyos'

class ObtInfoRocaInline(admin.StackedInline):
    extra = 1
    model =  ObtInfoRoca
    form = YacForms.ObtencionInfoForm
    suit_classes = 'suit-tab suit-tab-apoyos'


class ObservacionRocaInline(admin.StackedInline):
    model = ObservacRoca
    form = YacForms.ObservacionesForm
    extra = 1
    template = 'InlineTemplates/ObservacionesRoca.html'

class LlenadaPorRocaInline(admin.TabularInline):
    model = LlenadoRoca
    extra = 1
    suit_classes = 'suit-tab suit-tab-observaciones'


class SupervisadaPorRocaInline(admin.TabularInline):
    model = SupervisadoRoca
    extra = 1
    suit_classes = 'suit-tab suit-tab-observaciones'


########################################################################################
# Declaracion y registro de administradores
########################################################################################
    
#Administrador del modelo de datos Roca
#Usando los parametros de la extensión Suite, se mejora y organiza el admin

class RocaAdmin (admin.ModelAdmin):
    model = Roca
    form = forms.RocaForm
    #list_display = ('yacimiento', 'codigo', 'nombre', 'manifiestacionAsociada', 'estado')	 
    #list_filter = ('yacimiento', 'codigo', 'estado')

    fieldsets = [
        ('Datos generales de la Roca', {
            'classes': ('suit-tab suit-tab-generales',),
            'fields': ['yacimiento', 'codigo', 'nombre']
        }),
     ]



    inlines = [
        FotografiaRocaInline, Roca2Inline, CaraTrabajadaInline, DimensionRocaInline, UbicacionCarasInline, FigurasPorTipoInline,
        EsquemaPorCaraInline,ConexionFigurasInline, ManifestacionesInline, OtrosValRocaInline, TratFotoInline,
        FotoDigRocaInline,EscalaNatRocaInline, EscalaRedRocaInline, BibRocaInline, MatAudioVisualInline, VideoRocaInline,
        PeliculaRocaInline, PaginaWebRocaInline, MultimediaRocaInline, ObtInfoRocaInline,  ObservacionRocaInline,
        LlenadaPorRocaInline, SupervisadaPorRocaInline
    ]
    suit_form_tabs = (('generales', 'Datos Generales de la Roca'),
                      ('figuras', 'Figuras'),
                      ('tratamientos', 'Tratamiento para fotografia'),
                      ('manifestaciones', 'Manifestaciones Asociadas'),
                      ('apoyos', 'Apoyos'),
                      ('observaciones', 'Observaciones')                        
                      )	
    class Media:
        css = {
            "all": ("apps/Rocas/admin.css",)
        }
        js = ("apps/Rocas/admin.js",)

admin.site.register(Roca,RocaAdmin)
