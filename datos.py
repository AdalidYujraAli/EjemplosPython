#Leer datos desde archivo csv
import csv
nombre_archivo="informacion.csv"
#Convertir un puntaje en una letra:
def asignarLetra(puntaje):
  if puntaje>=90:
    letra="A"
  elif puntaje >=80:
    letra="B"
  elif puntaje>=70:
    letra="C"
  elif puntaje>=60:
    letra="D"
  else:
    letra="F"
  return letra

# #Abrir el archivo en "modo de lectura"
# #Esto permie manipular los archivos creados por programas como EXCEL
#
# archivo=open(nombre_archivo, "r")
#
# #Colocamos el lector de csv, para leer el archivo en FILAS
# csvConvertido=csv.reader(archivo)
#
# #Tratamos cada fila como una lista
# leerCabecera=True
# for fila in csvConvertido: #Iterar en cada línea
#   if leerCabecera:#Verificamos si es la primera línea
#     leerCabecera=False
#     continue#Saltamos la primera línea
#   #Mostramos el contenido original del archivo
#   #print("Original",fila)
#
#   nombre=fila[0]#guardar el nombre del estudiante
#   total=0#preparamos la variable para la nota
#   for index in range(1,7):#Iteramos a través de los 7 puntajes
#     curso=fila[index]
#     if curso=="":
#       curso=0.0
#     else:
#       curso=float(curso)
#     total=total+curso
#   porcentaje=(total*100)/200
#   reporteCurso=asignarLetra(porcentaje)
#   print(nombre," Porcentaje: ",porcentaje," Letra de Grado: ",reporteCurso)
# archivo.close()#Cerramos el archivo

nombre_archivo="informacion.csv"

with open(nombre_archivo, newline='') as csvfile:
    lector = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for fila in lector:
        print(', '.join(fila))
