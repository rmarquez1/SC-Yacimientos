import inspect

def has_attr(model, aname):
	return aname in model.__dict__

def get_type(model, aname):
	""" Retorna el tipo del atributo en modelo dado """
	
	if aname in model.__dict__:
		field = model._meta.get_field(aname)
		atype = field.get_internal_type()
	
		return atype
	return None

def get_attrs_wlabel(model):
	""" Retorna el nombre, tipo y etiqueta de cada atributo del modelo dado """

	for field in model._meta.fields:
		if field.name == 'id':
			continue
		
		name = model.abbr + '_' + field.name	
		atype = field.get_internal_type()
		label = field.verbose_name

		yield (name, atype, label)

def get_attrs(model):
	""" Retorna el nombre y tipo de cada atributo del modelo dado """

	for field in model._meta.fields:
		if field.name == 'id':
			continue
		
		name = model.abbr + '_' + field.name	
		atype = field.get_internal_type()

		yield (name, atype, field.name)


def get_models(module):
	""" Retorna todos los modelos declarados en el modulo dado """

	for name, model in inspect.getmembers(module):
		if inspect.isclass(model) and model.__module__ == module.__name__:
			yield (name, model)
			
