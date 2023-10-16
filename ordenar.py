a=int(input("Ingrese valor a: "))
b=int(input("Ingrese valor b: "))
c=int(input("Ingrese valor c: "))

mayor=a
mediano=b
menor=c

if mayor<b:
  mayor=b
  mediano=a
  if mediano<c:
    mediano=c
    menor=a
else:
  if mediano<c:
    mediano=c
    menor=a
print(mayor,mediano,menor)
