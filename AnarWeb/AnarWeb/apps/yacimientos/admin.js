/** 
* Funciones creadas para dar estilo y modificar las etiquetas del admin 
* que son creadas por suit y que puedan estar identadas por jerarquia.
* Se hace tomando en cuenta los puntos que están antes del espacio
*
*	Ej: 2.3 A
*			2.3.1 B
*		2.4 C	
****/

//Para que utilice el $jquery de Suit
(function ($){

	//Document Ready
	$(function () {
	
		// Solamente para los formularios de modificación y no los listados
		$('body.change-form').each(		
			function () {
				
				//Para cada uno de los fielsets que contienen varios control-labels						
				$("fieldset").each(
					function (indexlol) {	
						
						var min_index = null;				
						var current_index = null;
						var name = null;
						var $labels = $(this).find(".control-label label");
						
						//Para cada uno de los items del fieldset, se busca el menor indice
						$labels.each(
							function(){
															
								name = $(this).html();									
								name = name.substring(0, name.indexOf(' ')); //Se toman en cuanta sólo los puntos antes del espacio 2.3 a.aa
								current_index = (name.match(/\./g)||[]).length;									
								if (min_index == null || current_index < min_index ) {										
									min_index = current_index;
								}
								$(this).attr('suit-level', current_index);								
							}						
						);
						
						$labels.each(
							function(){
								
								//Se agregan clases que permiten identar: level1, level2, level3, level4 dependiendo del indice minimo
								current_index = $(this).attr('suit-level');
								if (current_index > min_index) {									
									$(this).addClass('level' + (current_index - min_index) );
								}							
							}						
						);
						
					}		
				);
			}
		);
	});	
}(Suit.$));


