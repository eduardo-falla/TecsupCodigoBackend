from typing import no_type_check_decorator


""" notas =(14,16,17,11,5,4,5,1)

print(notas[0])
print(notas[-1])
print(len(notas))
print(notas.count(5)) """

libro = { "nombre": "Harry Potter",
 "autor": "J.K. Rowling", 
 "editorial": "Blablabla", 
 "año": 2018, 
 "idiomas": [ { "nombre": "portuges" },
  { "nombre": "ingles", "nombre": "ingles britanico" },
   { "nombre": "frances" }, { "nombre": "aleman" }, ],
"calificacion": 5, "imdb": "00asd12-asd878-a4s5d4a5-a45sd4a5sd", 
"tomos": ("La piedra filosofal", "La camara secreta", "El vuelo del fenix") }
#Autor del libro
print(libro["autor"])
#Segundo tomo
print(libro["tomos"][1])
#Cantidad de idiomas
print(len(libro["idiomas"]))
#idioma ruso esta?
idioma="ruso"
if {"nombre":idioma} in libro["idiomas"] : 
    print(f"{idioma} Si se encuentra")
else:
    print(f"{idioma} no se encuentra")
