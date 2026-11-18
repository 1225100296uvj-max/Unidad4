################################## 
#Programa Uriel Villalobos Juárez#
##################################
 
def es_correo_valido(correo):
	if "@" not in correo:
		return False 

	if texto.count(“@”) > 1: 
		return False

	usuario,dominio = correo.split("@", 1) 

	if usuario == "" or "." not in dominio:
		return False

	return True

print(f"#"*46,"\n# Programa Uriel Villalobos Juárez - GTIR246 #\n", f"#"*46, sep = "")