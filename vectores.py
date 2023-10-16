#Llenamos el vector con valores leidos desde el teclado
vector=[]
try:
  a=int(input("Ingrese un valor: "))
  while a!=0:
    vector.append(a)
    a=int(input("Ingrese un valor: "))
  print(vector)
except:
  print("Ingrese valores válidos por favor")

#Seleccione una opción para realizar una operación sobre el vector
print("""
1: Suma
2: Producto
3: Orden Ascendente
4: Orden Descendente
5: Hallar el mayor
6: Hallar el menor
0: Salir del programa
""")
opcion=int(input("Seleccione una opción: "))
vector2=vector

#Creamos un archivo que almacenará la solución
archivo=open("miSolucion.txt","a")
while opcion!=0:
  texto="Vector original: "+"".join(map(str, vector))+"\n"
  archivo.write(texto)
  if opcion==1:
    suma = 0
    for i in vector:
      suma += i
    texto="\nLa suma del vector es: "+str(suma)+"\n"
    archivo.write(texto)
    print("Se agregó el resultado al archivo")
  elif opcion==2:
    producto=1
    for i in vector:
      producto*=i
    archivo.write("\nLa suma del vector es: ",producto)
    print("Se agregó el resultado al archivo")
  elif opcion==3:
    vector2.sort()
    archivo.write("\nLa suma del vector es: ",vector2)
    print("Se agregó el resultado al archivo")
  elif opcion==4:
    vector2.sort(reverse=True)
    archivo.write("\nLa suma del vector es: ",vector2)
    print("Se agregó el resultado al archivo")
  elif opcion==5:
    vector2.sort()
    solucion=vector2[len(vector2)-1]
    archivo.write("\nEl elemento más grande es: ",solucion)
    print("Se agregó el resultado al archivo")
  elif opcion==6:
    vector2.sort()
    solucion=vector2[0]
    archivo.write("\nEl elemento más pequeño del vector es: ",solucion)
    print("Se agregó el resultado al archivo")
  else:
    print("Fin del programa")
  opcion = int(input("Seleccione una opción: "))
archivo.close()
archivo=open("miSolucion.txt","r")
print(archivo.read())
archivo.close()
