from django.conf.urls import patterns, url

from AnarWeb.apps.yacimientos import views

urlpatterns = patterns('',
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    url(r'quienessomos/origen', views.quienessomosOrigenytrayectoria, name='origenytrayectoria'),
    url(r'quienessomos/areas', views.quienessomosAreasdeespecializacion, name='areasdeespecializacion'),
    url(r'quienessomos/proyectos', views.quienessomosProyectosactuales, name='proyectosactuales'),
    url(r'quienessomos/adjuntos', views.quienessomosProfesionalesadjuntos, name='profesionalesadjuntos'),
    url(r'patrimonio/ley', views.patrimoniorupestreLeydeproteccion, name='leydeproteccion'),
    url(r'patrimonio/pinturas', views.patrimoniorupestrePinturasrupestres, name='pinturasrupestres'),
    url(r'patrimonio/geoglifo', views.patrimoniorupestreGeoglifo, name='geoglifo'),
    url(r'patrimonio/petroglifo', views.patrimoniorupestrePetroglifo, name='petroglifo'),
    url(r'patrimonio/amoladores', views.patrimoniorupestreAmoladores, name='amoladores'),
    url(r'patrimonio/monumentos', views.patrimoniorupestreMonumentosmegaliticos, name='monumentosmegaliticos'),
    url(r'patrimonio/micropetroglifos', views.patrimoniorupestreMicropetroglifos, name='micropetroglifos'),
    url(r'patrimonio/piedrasycerros', views.patrimoniorupestrePiedrasycerrosmiticos, name='piedrasycerrosmiticos'),
    url(r'patrimonio/geoportal', views.patrimoniorupestreGeoportal, name='geoportal'),
    url(r'educacion/escuela', views.programadeeducacionLasmanifestacionesylaescuela, name='manifestacionesylaescuela'),
    url(r'educacion/convenios', views.programadeeducacionConvenios, name='convenios'),
    url(r'educacion/material', views.programadeeducacionMaterialdidactico, name='materialdidactico'),
    url(r'productosyservicios/publicaciones', views.productosyserviciosPublicaciones, name='publicaciones'),
    url(r'productosyservicios/productos', views.productosyserviciosProductos, name='productos'),
    url(r'productosyservicios/asesorias', views.productosyserviciosAsesorias, name='asesorias'),
    url(r'productosyservicios/visitas', views.productosyserviciosVisitasguiadas, name='visitasguiadas'),
    url(r'contacto', views.contacto, name='contacto'),
    )