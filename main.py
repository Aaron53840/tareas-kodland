traduccion = {
    "juicioso" : "persona responsable o que cumpla sus deberes",
    "canguil" : "maiz pira o plaomita de maiz",
    "palta" : "aguacate"
}

palabra = input ("ingresa una palabra en minuscula, que quieras traducir:")
if palabra in traduccion.keys():
    print("el significado es:", traduccion[palabra])

else:
    print("la palabra no existe")
