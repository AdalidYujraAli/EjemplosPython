notas=[]
while True:
  nombre=input("Ingrese un nombre: ")
  nota=int(input("Ingrese la nota: "))
  notas.append([nombre,nota])
  respuesta=input("Escriba s para salir del programa: ")
  if respuesta=='s':
    break
print(notas)
suma=0
n=[]
for x in notas:
  suma+=notas[notas.index(x)][1]
  n.append(notas[notas.index(x)][1])
promedio=suma/len(notas)
nMaxima=max(n)
nMinima=min(n)

print('El estudiante: ',notas[n.index(nMaxima)],' tiene la nota máxima: ',nMaxima)
print('El estudiante: ',notas[n.index(nMinima)],' tiene la nota máxima: ',nMinima)

