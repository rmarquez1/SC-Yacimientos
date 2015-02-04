# -*- coding: utf-8 -*-

from django import forms
from haystack.forms import SearchForm
from AnarWeb.apps.yacimientos.forms import OPCIONES_ESTADO, shortTextField, regularTextField, fullTextField, regularTextArea, regularSelect

#import AnarWeb.apps.Rocas.models
from AnarWeb.apps.yacimientos.models import CharField
import AnarWeb.apps.yacimientos.dynamic

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

        if dynamic.get_type(mclass, 'yacimiento') == 'ForeignKey' or dynamic.has_attr(mclass, 'roca'):
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

### Formularios utilizados por el backend para roca        
class RocaForm(BaseForm):
    yacimiento      = forms.CharField(required=False, max_length=20)
    codigo                             = forms.CharField(required=False, max_length=20)
    nombre                     = forms.CharField(required=False, max_length=150)
    estado                         = forms.MultipleChoiceField(required=False, choices=OPCIONES_ESTADO)
    figuras                             = forms.CharField(required=False, max_length=100)
    otros                         = forms.CharField(required=False, max_length=150)    

class DimensionRocaForm(ModelForm) :

    class Meta:
        widgets = {
        		'dimensiones': TextInput(attrs={'class': 'input-medium'}),            
                'alto': TextInput(attrs={'class': 'input-small'}),
                'largo': TextInput(attrs={'class': 'input-small'}),
            	'ancho': TextInput(attrs={'class': 'input-small'}),
        }
  
class ManifestacionesAsociadasForm(ModelForm):

	class Meta:
		widgets = {
				'hasMitos' : TextInput(attrs=regularTextField),
				'hasOtros' : TextInput(attrs=regularTextField),
		}

class UbicacionCarasForm(ModelForm) :

    class Meta:
        widgets = {                
                'bocaPrincipal':  TextInput(attrs=regularTextField),
                'altura': TextInput(attrs=regularTextField),                 
        }


class FigurasPorTipoForm (ModelForm):
    class Meta:
        widgets = {
            'numero': TextInput(attrs={'class': 'input-medium'}),
            'cantidad': TextInput(attrs={'class': 'input-small'}),
            'tipoFigura': Select(attrs={'class': 'input-medium'}),
            'numero': TextInput(attrs={'class': 'input-small'}),
            'esCantidadInexacta' : TextInput(attrs={'class': 'input-small'}),
            'descripcion' : AutosizedTextarea(attrs={'rows': 2})
        }			
	
class CaraTrabajadaForm (ModelForm):
    class Meta:
        widgets = {
            'numero': TextInput(attrs={'class': 'input-medium'}),
            'orientacion': Select(attrs={'class': 'input-medium'})
        }
		
class RocaForm(ModelForm) :

    class Meta:
        widgets = {
                'yacimiento': LinkedSelect,
                'codigo': TextInput(attrs=regularTextField),
                'nombre': TextInput(attrs=regularTextField),
        }


class RepGrafRocaForm(ModelForm) :
    class Meta:
        widgets = {                
                'numPiezas': TextInput(attrs=shortTextField),
                'instituto': TextInput(attrs=fullTextField),
                'persona': TextInput(attrs=fullTextField),
                'tipoReproduccion' : Select(attrs=regularSelect)
        }

class TratFotoRocaForm(ModelForm) :
    class Meta:
        widgets = {                
                'limpiezaCon': AutosizedTextarea(attrs=regularTextArea),
                'rellenoSurcos': AutosizedTextarea(attrs=regularTextArea),
                'tratamientoDigital': AutosizedTextarea(attrs=regularTextArea),
                'programaVersion' : AutosizedTextarea(attrs=regularTextArea),
                'otrosTratamientos' : AutosizedTextarea(attrs=regularTextArea),
                
        }   
