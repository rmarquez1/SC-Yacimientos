# -*- coding: utf-8 -*-

from django import forms
from haystack.forms import SearchForm

import AnarWeb.apps.yacimientos.models


import dynamic

from django.forms import ModelForm
from suit.widgets import LinkedSelect, AutosizedTextarea, TextInput, Select



class BaseForm(SearchForm):
    # Busqueda
    def search(self):
        sqs = super(BaseForm, self).search()
        print sqs


        if not self.is_valid():
            return self.no_query_found()

        filters = {}
        for field, value in self.cleaned_data.items():
            if self.cleaned_data[field]:
                if isinstance(value, list):
                    filters[field + '__in'] = value 
                else:
                    filters[field] = value

        return sqs.filter(**filters)


def crear_form(classes, name):
    """ Crea un FORM con todos los atributos de las clases dadas """

    attrs   = {}
    
    for fclass in classes:
        mclass = getattr(anarapp.models, fclass)

        if dynamic.get_type(mclass, 'yacimiento') == 'ForeignKey' or dynamic.has_attr(mclass, 'piedra'):
            foreign.append(mclass.abbr)
        
        for fname, ftype, flabel in dynamic.get_attrs_wlabel(mclass):
            if ftype == 'CharField':
                attrs[fname] = forms.CharField(required=False, max_length=100, label=flabel)
            elif ftype == 'IntegerField':
                attrs[fname] = forms.IntegerField(required=False, label=flabel)
            elif ftype == 'BooleanField':
                attrs[fname] = forms.BooleanField(required=False, label=flabel)         
            elif ftype == 'DateField':
                attrs[fname] = forms.DateField(required=False, label=flabel)
    attrs['valor'] = forms.CharField(required=False, max_length=100)

    return type(name, (BaseForm,), attrs)

########################################################################################
# Creando Basic Form
########################################################################################

OPCIONES_MANIFESTACION = (
    (1,        'Geoglifo'),
    (2,        'Pintura Rupestre'),
    (3,        'Petroglifo'),
    (4,        'Petroglifo Pintado'),
    (5,        'Micro-Petroglifo'),
    (6,        'Piedra Mítica Natural'),
    (7,        'Cerro Mítico Natural'),
    (8,        'Cerro Mitico Natural con Petroglifo'),
    (9,        'Cerro Mitico Natural Con Pintura'),
    (10,'Cerro Mitico Natural Con Dolmen'),
    (11,'Monumentos Megalíticos'),
    (12,'Monolitos'),
    (13,'Monolitos Con Grabados'),
    (14,'Menhires'),
    (15,'Menhires Con Puntos Acoplados'),
    (16,'Menhires Con Petroglifo'),
    (17,'Menhires Con Pintura'),
    (18,'Amolador'),
    (19,'Batea'),
    (20,'Puntos Acoplados'),
    (21,'Cupulas'),
    (22,'Mortero o Metate'),
)  

class BasicForm(BaseForm):
        manifestacion         = forms.MultipleChoiceField(required=False, choices=OPCIONES_MANIFESTACION)
        
        # Seleccion Multiple
        manifestacion.widget.attrs         = {'class':'chzn-select', 'data-placeholder':'Seleccione el tipo de manifestación'}


########################################################################################
# Creando Advanced Form
########################################################################################


OPCIONES_ESTADO = (
        ('Amazonas'        , 'Amazonas'),
        ('Anzoategui', 'Anzoategui'),
        ('Apure', 'Apure'),
        ('Aragua', 'Aragua'),
        ('Barinas', 'Barinas'),
        ('Bolívar', 'Bolívar'),
        ('Carabobo', 'Carabobo'),
        ('Cojedes', 'Cojedes'),
        ('Delta Amacuro', 'Delta Amacuro'),
        ('Falcón', 'Falcón'),
        ('Guárico', 'Guárico'),
        ('Lara', 'Lara'),
        ('Mérida', 'Mérida'),
        ('Miranda', 'Miranda'),
        ('Monagas', 'Monagas'),
        ('Nueva Esparta', 'Nueva Esparta'),
        ('Portuguesa', 'Portuguesa'),
        ('Sucre', 'Sucre'),
        ('Tachira', 'Tachira'),
        ('Trujillo', 'Trujillo'),
        ('Vargas', 'Vargas'),
        ('Yaracuy', 'Yaracuy'),
        ('Zulia', 'Zulia'),
)

OPCIONES_TIPO = (
        (1, 'Pared Rocosa'),
    (2, 'Roca'),
    (3, 'Dolmen(natural)'),
    (4, 'Abrigo'),
    (5, 'Cueva'),
    (6, 'Cueva de Recubrimiento'),
    (7, 'Terreno Superficial'),
    (8, 'Terreno Profundo'),
)

OPCIONES_EXPOSICION = (
        (1, 'Expuesto'),
    (2, 'No Expuesto'),
    (3, 'Expuesto Periodicamente'),
)

OPCIONES_UBICACION = (
    (1, 'Cerro'),
    (2, 'Valle'),
    (3, 'Río'),
    (4, 'Costa'),
)

OPCIONES_MATERIAL = (
         (1, 'Roca'),
    (2, 'Tierra'),
    (3, 'Hueso'),
    (4, 'Corteza de árbol'),
    (5, 'Pieles'),
)

OPCIONES_CONSERVACION = (
        (1, 'Bueno'),
        (2, 'Modificado'),
)

OPCIONES_MANIF_ASOCIADAS = (
        (1, 'Lítica'),
        (2, 'Cerámica'),
        (3, 'Oseo'),
        (4, 'Concha'),
        (5, 'Carbón No Superficial'),
        (6, 'Mitos'),
        (7, 'Cementerios'),
        (8, 'Montículos'),

)



class AdvancedForm(BasicForm):

        codigo                             = forms.CharField(required=False, max_length=20)
        municipio                 = forms.CharField(required=False, max_length=150)
        estado                         = forms.MultipleChoiceField(required=False, choices=OPCIONES_ESTADO)
        nombre                         = forms.CharField(required=False, max_length=100)
        localidad                     = forms.CharField(required=False, max_length=150)
        fotografia                 = forms.BooleanField(required=False)
        tipo                                 = forms.MultipleChoiceField(required=False, choices=OPCIONES_TIPO)
        exposicion                 = forms.MultipleChoiceField(required=False, choices=OPCIONES_EXPOSICION)
        
        ubicacion                 = forms.MultipleChoiceField(required=False, choices=OPCIONES_UBICACION)
        material                     = forms.MultipleChoiceField(required=False, choices=OPCIONES_MATERIAL)
        conservacion         = forms.MultipleChoiceField(required=False, choices=OPCIONES_CONSERVACION)
        
        manifasociadas         = forms.MultipleChoiceField(required=False, choices=OPCIONES_MANIF_ASOCIADAS)
        
        #Seleccion multiple
        estado.widget.attrs                          = {'class':'chzn-select', 'data-placeholder':'Seleccione el estado'}
        tipo.widget.attrs                                  = {'class':'chzn-select', 'data-placeholder':'Seleccione el tipo de yacimiento'}
        exposicion.widget.attrs             = {'class':'chzn-select', 'data-placeholder':'Seleccione el tipo de exposición'}
        ubicacion.widget.attrs                     = {'class':'chzn-select', 'data-placeholder':'Seleccione la ubicación'}
        material.widget.attrs                      = {'class':'chzn-select', 'data-placeholder':'Seleccione el tipo de material'}
        conservacion.widget.attrs         = {'class':'chzn-select', 'data-placeholder':'Seleccione el estado de conservación'}
        manifasociadas.widget.attrs = {'class':'chzn-select', 'data-placeholder':'Seleccione las manifetaciones asociadas'}



class YacimientoForm(forms.ModelForm):
        pass





shortTextField = {'class': 'input-small', 'style': 'width:75%'}
regularTextField = {'class': 'input-medium', 'style': 'width:75%'}
fullTextField = {'class': 'input-medium', 'style': 'width:95%'}
regularTextArea = {'rows': 4, 'style': 'width:75%'}
regularSelect = {'class': 'input-medium'}


### Formularios utilizados por el backend para yacimiento
class YacimientoForm(ModelForm) :

    class Meta:
        widgets = {
                'codigo': TextInput(attrs=regularTextField),
        'nombre': TextInput(attrs=regularTextField),
        'pais': TextInput(attrs=regularTextField),
        }

class LocalidadYacimientoForm(ModelForm) :
    class Meta:
        widgets = {
                'nombrePoblado': TextInput(attrs=regularTextField),
        'nombreNoPoblado': TextInput(attrs=regularTextField),
        }   

class TenenciaDeTierraForm(ModelForm) :
    class Meta:
        widgets = {
                'esTenenciaOtros': TextInput(attrs=regularTextField),
        }

class IndicacionesForm(ModelForm) :
    class Meta:
        widgets = {
                'direcciones': AutosizedTextarea(attrs=regularTextArea),
                'puntoDatum': AutosizedTextarea(attrs=regularTextArea),
        }
            
class PlanoForm(ModelForm) :
    class Meta:
        widgets = {
                'numeroPlano': TextInput(attrs=regularTextField),
        }
        
class CoordenadasForm(ModelForm) :
    class Meta:
        widgets = {
                'longitud': TextInput(attrs=fullTextField),
                'latitud': TextInput(attrs=fullTextField),
                'utmAdicional': TextInput(attrs=fullTextField),
        }

class AltitudForm(ModelForm) :
    class Meta:
        widgets = {
                'texto': TextInput(attrs=regularTextField),
        'altura': TextInput(attrs=regularTextField),
        'superficie': TextInput(attrs=regularTextField),
        'desarrollo': TextInput(attrs=regularTextField),
        'desnivel': TextInput(attrs=regularTextField),
        }        

class TexturaSueloForm(ModelForm) :
    class Meta:
        widgets = {
                'mixto': TextInput(attrs=regularTextField),            
        }

class FloraYacimientoForm(ModelForm) :
    class Meta:
        widgets = {
                'flora': AutosizedTextarea(attrs=regularTextArea),
        }

class FaunaYacimientoForm(ModelForm) :
    class Meta:
        widgets = {
                'fauna': AutosizedTextarea(attrs=regularTextArea),
        }

class HidrologiaYacimientoForm(ModelForm) :
    class Meta:
        widgets = {
                'otros': TextInput(attrs=regularTextField),
        'nombre': TextInput(attrs=regularTextField),
        'distancia': TextInput(attrs=regularTextField),
        'observaciones': AutosizedTextarea(attrs=regularTextArea),
        }

class TipoExposicionYacForm(ModelForm) :
    class Meta:
        widgets = {
        'observaciones': AutosizedTextarea(attrs=regularTextArea),
        }

class ConstitucionYacimientoForm(ModelForm) :
    class Meta:
        widgets = {
                'nroPiedras': TextInput(attrs=regularTextField),
        'nroPiedrasGrabadas': TextInput(attrs=regularTextField),
        'nroPiedrasPintadas': TextInput(attrs=regularTextField),
                'nroPiedrasColocadas': TextInput(attrs=regularTextField),
        'otros': TextInput(attrs=regularTextField)
        }

class OrientacionYacimientoForm(ModelForm) :
    class Meta:
        widgets = {
                'otros': TextInput(attrs=regularTextField),
        'orientacion': TextInput(attrs=regularTextField),
        }

class MaterialYacimientoForm(ModelForm) :
    class Meta:
        widgets = {
                'tipo': TextInput(attrs=regularTextField),
        'otros': TextInput(attrs=regularTextField),
        }

class TecnicaParaGeoglifoForm(ModelForm) :
    class Meta:
        widgets = {
                'tecnicas': AutosizedTextarea(attrs=regularTextArea),
        }

class TecnicaParaPinturaForm(ModelForm) :
    class Meta:
        widgets = {
                'otros': AutosizedTextarea(attrs=regularTextArea),
        }
        
class TecnicaParaPetroglifoForm(ModelForm) :
    class Meta:
        widgets = {
                'otros': AutosizedTextarea(attrs=regularTextArea),
        }

class TecnicaParaMicroPetroForm(ModelForm) :
    class Meta:
        widgets = {
                'otros': AutosizedTextarea(attrs=regularTextArea),
        }
        
class TecnicaParaMonumentosForm(ModelForm) :
    class Meta:
        widgets = {
                'tecnicas': AutosizedTextarea(attrs=regularTextArea),
                'otros': AutosizedTextarea(attrs=regularTextArea),
        }

class CaracSurcoPetroglifoForm(ModelForm) :
    class Meta:
        widgets = {
                'anchoDe': TextInput(attrs=regularTextField),
                'anchoA': TextInput(attrs=regularTextField),
                'produndidadDe': TextInput(attrs=regularTextField),
                'profundidadA': TextInput(attrs=regularTextField),
        }
        
class CaracSurcoAmoladoresForm(ModelForm) :
    class Meta:
        widgets = {
                'largo': TextInput(attrs=regularTextField),
                'ancho': TextInput(attrs=regularTextField),
                'diametro': TextInput(attrs=regularTextField),                
        }

class CaracSurcoBateasForm(ModelForm) :
    class Meta:
        widgets = {
                'largo': TextInput(attrs=regularTextField),
                'ancho': TextInput(attrs=regularTextField),
                'diametro': TextInput(attrs=regularTextField),
                'profundidad': TextInput(attrs=regularTextField),                
        }

class CaracSurcoPuntosAcoplForm(ModelForm) :
    class Meta:
        widgets = {
                'diametro': TextInput(attrs=regularTextField),
                'profundidad': TextInput(attrs=regularTextField),
                'otros': AutosizedTextarea(attrs=regularTextArea),                
        }

class CaracSurcoCupulasForm(ModelForm) :
    class Meta:
        widgets = {
                'largo': TextInput(attrs=regularTextField),
                'ancho': TextInput(attrs=regularTextField),
                'diametro': TextInput(attrs=regularTextField),
                'profundidad': TextInput(attrs=regularTextField),
                'otros': AutosizedTextarea(attrs=regularTextArea),                
        }

class CaracSurcoMorteroForm(ModelForm) :
    class Meta:
        widgets = {
                'largo': TextInput(attrs=regularTextField),
                'ancho': TextInput(attrs=regularTextField),                
        }

class CaracDeLaPinturaForm(ModelForm) :
    class Meta:
        widgets = {
                'otros': AutosizedTextarea(attrs=regularTextArea),                
                'anchoDe': TextInput(attrs=regularTextField),
                'anchoA': TextInput(attrs=regularTextField),
                'anchoDeComp': TextInput(attrs=regularTextField),
                'anchoAComp': TextInput(attrs=regularTextField),
        }

class ColoresForm(ModelForm) :

    class Meta:
        widgets = {                
                'c':  TextInput(attrs=shortTextField),
                'm': TextInput(attrs=shortTextField),
                'y': TextInput(attrs=shortTextField),                    
                'k': TextInput(attrs=shortTextField),                    
        }
                
        
class CaracMonolitosForm(ModelForm) :
    class Meta:
        widgets = {                
                'cantidad': TextInput(attrs=regularTextField),
                'cantidadConGrabados': TextInput(attrs=regularTextField),
        }

class CaracMenhiresForm(ModelForm) :
    class Meta:
        widgets = {                
                'cantidadPiedrasVerticales': TextInput(attrs=regularTextField),
                'cantidadConPuntosAcoplados': TextInput(attrs=regularTextField),
                'cantidadConPetroglifo': TextInput(attrs=regularTextField),
                'cantidadConPinturas': TextInput(attrs=regularTextField),
                'distanciamiento': TextInput(attrs=regularTextField),
        }

class CaracDolmenArtForm(ModelForm) :
    class Meta:
        widgets = {                
                'cantidadConPetroglifo': TextInput(attrs=regularTextField),
                'cantidadConPinturas': TextInput(attrs=regularTextField),                
        }
        
class NotasYacimientoForm(ModelForm) :
    class Meta:
        widgets = {                
                'notas': AutosizedTextarea(attrs=regularTextArea),                
        }

class EstadoConserYacForm(ModelForm) :
    class Meta:
        widgets = {                
                'trasladado': TextInput(attrs=regularTextField),
                'trasladadoPa': TextInput(attrs=regularTextField),
                'sumergido': TextInput(attrs=regularTextField),
                'sumergidoPa': TextInput(attrs=regularTextField),
                'enterrado': TextInput(attrs=regularTextField),
                'enterradoPa': TextInput(attrs=regularTextField),
                'perdido': TextInput(attrs=regularTextField),
                'perdidoPa': TextInput(attrs=regularTextField),
                'destruido': TextInput(attrs=regularTextField),
                'destruidoPa': TextInput(attrs=regularTextField),
                'crecimientoVeg': TextInput(attrs=regularTextField),
                'crecimientoVegPa': TextInput(attrs=regularTextField),
                'patina': TextInput(attrs=regularTextField),
                'patinaPa': TextInput(attrs=regularTextField),
                'erosion': TextInput(attrs=regularTextField),
                'erosionPa': TextInput(attrs=regularTextField),
                'especificar': AutosizedTextarea(attrs=regularTextArea),                
        }


class CausasDestruccionYacForm(ModelForm) :
    class Meta:
        widgets = {   
                'otros': AutosizedTextarea(attrs=regularTextArea),
        }       

class IntensidadDestruccionYacForm(ModelForm) :
    class Meta:
        widgets = {   
                'observaciones': AutosizedTextarea(attrs=regularTextArea),
                'mas': TextInput(attrs=regularTextField),       
        }           
        
class ConsiderTempForm(ModelForm) :
    class Meta:
        widgets = {                
                'otros': AutosizedTextarea(attrs=regularTextArea),
        }

class CronologiaTentativaForm(ModelForm) :
    class Meta:
        widgets = {                
                'autor': TextInput(attrs=regularTextField),
                'fecha': TextInput(attrs=regularTextField),
                'institucion': TextInput(attrs=regularTextField),
                'pais': TextInput(attrs=regularTextField),
                'direccion': AutosizedTextarea(attrs=regularTextArea),
                'telefono': TextInput(attrs=regularTextField),
                'mail': TextInput(attrs=regularTextField),
                'tecnica':  AutosizedTextarea(attrs=regularTextArea),
                'bibliografia': AutosizedTextarea(attrs=regularTextArea),
                'twitter': TextInput(attrs=regularTextField),
                'facebook': TextInput(attrs=regularTextField),
        }


class ManifestacionesAsociadasForm(ModelForm) :
    class Meta:
        widgets = {                
                'descripcionLitica': AutosizedTextarea(attrs=regularTextArea),
                'descripcionCeramica': AutosizedTextarea(attrs=regularTextArea),
                'descripcionOseo': AutosizedTextarea(attrs=regularTextArea),
                'descripcionConcha': AutosizedTextarea(attrs=regularTextArea),
                'descripcionCarbon': AutosizedTextarea(attrs=regularTextArea),                
                'descripcionMito': AutosizedTextarea(attrs=regularTextArea),
                'descripcionCementerio': AutosizedTextarea(attrs=regularTextArea), 
                'descripcionMonticulo': AutosizedTextarea(attrs=regularTextArea),         
                'otros':  AutosizedTextarea(attrs=regularTextArea),
        }

class ManifestacionesLiticaForm(ModelForm) :
    class Meta:
        widgets = {                
                'descripcionLitica': AutosizedTextarea(attrs=regularTextArea),
        }

class ManifestacionesCeramicaForm(ModelForm) :
    class Meta:
        widgets = {                
                'descripcionCeramica': AutosizedTextarea(attrs=regularTextArea),        
        }

class ManifestacionesOseoForm(ModelForm) :
    class Meta:
        widgets = {                
                'descripcionOseo': AutosizedTextarea(attrs=regularTextArea),        
        }

class ManifestacionesConchaForm(ModelForm) :
    class Meta:
        widgets = {                
                'descripcionConcha': AutosizedTextarea(attrs=regularTextArea),        
        }

class ManifestacionesCarbonForm(ModelForm) :
    class Meta:
        widgets = {                
                'descripcionCarbon': AutosizedTextarea(attrs=regularTextArea),                        
        }

class ManifestacionesMitoForm(ModelForm) :
    class Meta:
        widgets = {                
                'descripcionMito': AutosizedTextarea(attrs=regularTextArea),        
        }

class ManifestacionesCementerioForm(ModelForm) :
    class Meta:
        widgets = {                
                'descripcionCementerio': AutosizedTextarea(attrs=regularTextArea),         
        }

class ManifestacionesMonticuloForm(ModelForm) :
    class Meta:
        widgets = {                
                'descripcionMonticulo': AutosizedTextarea(attrs=regularTextArea),         
        }

class ManifestacionesOtrosForm(ModelForm) :
    class Meta:
        widgets = {                
                'otros':  AutosizedTextarea(attrs=regularTextArea),
        }
                
class OtrosValForm(ModelForm) :
    class Meta:
        widgets = {                               
                'texto':  AutosizedTextarea(attrs=regularTextArea),
        }

class ObservacionesForm(ModelForm) :
    class Meta:
        widgets = {                               
                'texto':  TextInput(attrs=regularTextArea),
        }

### Formularios para las clases de multimedia
class FotoForm(ModelForm) :
    class Meta:
        widgets = {                
                'negativo': TextInput(attrs=regularTextField),
                'tipoFotografia': TextInput(attrs=regularTextField),
                'fotografo': TextInput(attrs=regularTextField),
                'institucion': TextInput(attrs=regularTextField),
                'numReferencia': TextInput(attrs=regularTextField),                
                'numRollo': TextInput(attrs=regularTextField),
                'numFoto': TextInput(attrs=regularTextField),                
                'numMarcaNegativo': TextInput(attrs=regularTextField),
                'numCopiaAnar': TextInput(attrs=regularTextField),  
        }
        
class BibliografiaForm(ModelForm) :
    class Meta:
        widgets = {                
                'codigo': TextInput(attrs=regularTextField),
                'titulo': TextInput(attrs=regularTextField),
                'autor': TextInput(attrs=regularTextField),
                'ano': TextInput(attrs=regularTextField),
                'institucion': TextInput(attrs=regularTextField),                                
                'descripcion': TextInput(attrs=regularTextField)
        }

class MatAudioVisualForm(ModelForm) :
    class Meta:
        widgets = {                
                'formato': TextInput(attrs=regularTextField)
        }

class VideoForm(ModelForm) :
    class Meta:
        widgets = {                
                'anio': TextInput(attrs=regularTextField),
                'formato': TextInput(attrs=regularTextField),
                'titulo': TextInput(attrs=regularTextField),
                'autor': TextInput(attrs=regularTextField),
                'institucion': TextInput(attrs=regularTextField),                
                'numReferencia': TextInput(attrs=regularTextField),
                'numCopia': TextInput(attrs=regularTextField),
        }

class PaginaWebForm(ModelForm) :
    class Meta:
        widgets = {                
                'direccionURL': TextInput(attrs=regularTextField)
        }

class MultimediaForm(ModelForm) :
    class Meta:
        widgets = {                
                'tecnica': TextInput(attrs=regularTextField)
        }

class ObtencionInfoForm(ModelForm) :
    class Meta:
        widgets = {                
                'nombre': TextInput(attrs=regularTextField),
                'direccion':  AutosizedTextarea(attrs=regularTextArea),
                'telefono': TextInput(attrs=regularTextField),
                'telefonoCel': TextInput(attrs=regularTextField),
                'mail': TextInput(attrs=regularTextField),
                'paginaWeb': TextInput(attrs=regularTextField),                
                'twitter': TextInput(attrs=regularTextField),
                'nombreFacebook': TextInput(attrs=regularTextField),
                'blog': TextInput(attrs=regularTextField)      
        }
        
   


