def validaSexo(cadena):
    result = False
    if cadena == "V" or cadena == "M":
        result = True
    return result

def pedirNombre():
    nombre = input("¿Cómo te llamas?: ")
    
def pedirSexo():
    sexo = input("Disculpa la pregunta tonta pero... ¿Eres mujer o varón?(V/M): ")
    while validaSexo(sexo) == False:
        print("...")
        sexo = input("Disculpa, pero no te entiendo, ¿mujer o varón?(V/M): ")
            
nombre = pedirNombre()
sexo = pedirSexo()