#Creador de frases
import random

listaNombres=["Juan","Ramiro","Andrea","Maria","Susana","Daniel","Felipe","Lina","Carlos","Noemi"]
nNombres=len(listaNombres)
print(listaNombres)
print(nNombres)
listaVerbos=['come','estudia','lee','corre','rie','juega','escribe','mira','pide']
nVerbos=len(listaVerbos)
print(listaVerbos)
print(nVerbos)
listaAdjetivos=['rojo','grande','pequeño','lindo','oscuro','claro','electrónico','viejo','nuevo','lento']
nAdjetivos=len(listaAdjetivos)
print(listaAdjetivos)
print((nAdjetivos))
listaSustantivos=['libro','cuaderno','informe','computadora','celular','auto','casa','reporte','lapiz','bolígrafo']
nSustantivos=len(listaSustantivos)
print(listaSustantivos)
print(nSustantivos)
while True:
  nombreIndice=random.randrange(0,nNombres)
  nombre=listaNombres[nombreIndice]
  verboIndice=random.randrange(0,nVerbos)
  verbo=listaVerbos[verboIndice]
  adjetivoIndice=random.randrange(0,nAdjetivos)
  adjetivo=listaAdjetivos[adjetivoIndice]
  sustantivoIndice=random.randrange(0,nSustantivos)
  sustantivo=listaSustantivos[sustantivoIndice]

  oracion=nombre+' '+verbo+' en su '+sustantivo+' '+adjetivo+'.'
  print(oracion)
  respuesta=input('Escriba s, para salir del programa')
  if respuesta=='s':
    break
print('Adiós')