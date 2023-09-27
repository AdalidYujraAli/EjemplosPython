a = int(input("Ingrese el primer número"))
b = int(input("Ingrese el segundo número"))
c = int(input("Ingrese el tercer número"))
if a>b and a>c:
  if b>c:
    print(a,b,c)
  else:
    print(a,c,b)
else:
  if b>a and b>c:
    if a>c:
      print(b,a,c)
    else:
      print(b,c,a)
  else:
    if c>a and a>b:
      print(c,a,b)
    else:
      print(c,b,a)

#Utilizando un capturador de errores
# try:
#   a = int(input("Ingrese el primer número"))
#   b = int(input("Ingrese el segundo número"))
#   c = int(input("Ingrese el tercer número"))
#   if a > b and a > c:
#     if b > c:
#       print(a, b, c)
#     else:
#       print(a, c, b)
#   else:
#     if b > a and b > c:
#       if a > c:
#         print(b, a, c)
#       else:
#         print(b, c, a)
#     else:
#       if c > a and a > b:
#         print(c, a, b)
#       else:
#         print(c, b, a)
# except:
#   print("Por favor ingrese un número válido")