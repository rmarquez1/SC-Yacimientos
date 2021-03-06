BEGIN;

DROP TABLE "yacimientos_constitucionyacimiento";
DROP TABLE "yacimientos_tipoexposicionyac";
DROP TABLE "yacimientos_hidrologiayacimiento";
DROP TABLE "yacimientos_faunayacimiento";
DROP TABLE "yacimientos_florayacimiento";
DROP TABLE "yacimientos_texturasuelo";
DROP TABLE "yacimientos_yacimiento";
DROP TABLE "yacimientos_municipio";
DROP TABLE "yacimientos_estado";


DROP TABLE "DatosGenerales_tipoyacimiento";
DROP TABLE "DatosGenerales_fotografiayac";
DROP TABLE "DatosGenerales_altitud";
DROP TABLE "DatosGenerales_datum";
DROP TABLE "DatosGenerales_coordenadas";
DROP TABLE "DatosGenerales_plano";
DROP TABLE "DatosGenerales_croquis";
DROP TABLE "DatosGenerales_indicaciones";
DROP TABLE "DatosGenerales_tenenciadetierra";
DROP TABLE "DatosGenerales_usoactsuelo";
DROP TABLE "DatosGenerales_localidadyacimiento";

DROP TABLE "LaManifestacion_materialyacimiento";
DROP TABLE "LaManifestacion_orientacionyacimiento";
DROP TABLE "LaManifestacion_ubicacionyacimiento";
DROP TABLE "LaManifestacion_manifestacionyacimiento";

DROP TABLE "Tecnicas_notasyacimiento";
DROP TABLE "Tecnicas_caracdolmenart";
DROP TABLE "Tecnicas_caracmenhires";
DROP TABLE "Tecnicas_caracmonolitos";
DROP TABLE "Tecnicas_desccolores";
DROP TABLE "Tecnicas_colores";
DROP TABLE "Tecnicas_caracdelapintura";
DROP TABLE "Tecnicas_caracsurcomortero";
DROP TABLE "Tecnicas_caracsurcocupulas";
DROP TABLE "Tecnicas_caracsurcopuntosacopl";
DROP TABLE "Tecnicas_caracsurcobateas";
DROP TABLE "Tecnicas_caracsurcoamoladores";
DROP TABLE "Tecnicas_caracsurcopetroglifo";
DROP TABLE "Tecnicas_tecnicaparamonumentos";
DROP TABLE "Tecnicas_tecnicaparamicropetro";
DROP TABLE "Tecnicas_tecnicaparapetroglifo";
DROP TABLE "Tecnicas_tecnicaparapintura";
DROP TABLE "Tecnicas_tecnicaparageoglifo";

DROP TABLE "Conservacion_cronologiatentativa";
DROP TABLE "Conservacion_considertemp";
DROP TABLE "Conservacion_intensidaddestruccionyac";
DROP TABLE "Conservacion_causasdestruccionyac";
DROP TABLE "Conservacion_estadoconseryac";

DROP TABLE "ManifestacionesAsociadas_otrosvalyac";
DROP TABLE "ManifestacionesAsociadas_otrosvalores";
DROP TABLE "ManifestacionesAsociadas_manifestacionesotros";
DROP TABLE "ManifestacionesAsociadas_manifestacionesmonticulo";
DROP TABLE "ManifestacionesAsociadas_manifestacionescementerio";
DROP TABLE "ManifestacionesAsociadas_manifestacionesmito";
DROP TABLE "ManifestacionesAsociadas_manifestacionescarbon";
DROP TABLE "ManifestacionesAsociadas_manifestacionesconcha";
DROP TABLE "ManifestacionesAsociadas_manifestacionesoseo";
DROP TABLE "ManifestacionesAsociadas_manifestacionesceramica";
DROP TABLE "ManifestacionesAsociadas_manifestacioneslitica";
DROP TABLE "ManifestacionesAsociadas_manifestacionesasociadas";

DROP TABLE "Apoyos_obtinfoyac";
DROP TABLE "Apoyos_obtencioninfo";
DROP TABLE "Apoyos_multimediayac";
DROP TABLE "Apoyos_multimedia";
DROP TABLE "Apoyos_paginawebyac";
DROP TABLE "Apoyos_paginaweb";
DROP TABLE "Apoyos_peliyacimiento";
DROP TABLE "Apoyos_pelicula";
DROP TABLE "Apoyos_videoyacimiento";
DROP TABLE "Apoyos_video";
DROP TABLE "Apoyos_matavyacimiento";
DROP TABLE "Apoyos_mataudiovisual";
DROP TABLE "Apoyos_bibyacimiento";
DROP TABLE "Apoyos_bibliografia";

DROP TABLE "Observaciones_supervisadoyac";
DROP TABLE "Observaciones_supervisadopor";
DROP TABLE "Observaciones_llenadoyac";
DROP TABLE "Observaciones_llenadopor";
DROP TABLE "Observaciones_observacionesyac";
DROP TABLE "Observaciones_observaciones";

COMMIT;
