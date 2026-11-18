def test_correo_valido():
	assert es_correo_valido("alumno@escuela.org") == True 

def test_sin_arroba(): 
	assert es_correo_valido("alumno.escuela.org") == False 

def test_dominio_sin_punto(): 
	assert es_correo_valido("alumno@escuela") == False 

def test_usuario_vacio(): 
	assert es_correo_valido("@escuela.org") == False

def test_doble_arroba():
	assert es_correo_valido("alumno@escuela@nose.org") == False

##

def es_correo_valido(correo):
	if "@" not in correo:
		return False 

	arroba = "@"
	if correo.count(arroba) > 1: 
		return False	

	usuario,dominio = correo.split("@", 1) 

	if usuario == "" or "." not in dominio:
		return False

	return True

##
print(f"#"*46,"\n# Programa Uriel Villalobos Juárez - GTIR246 #\n", f"#"*46, sep = "")