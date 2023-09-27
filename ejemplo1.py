try:
   a=int(input("ingrese a"))
   print(type(a))
   b=int(input("ingrese b"))
   print(type(b))
   suma=a+b
   resta=a-b
   multiplicacion=a*b
   division=a/b
   modulo=a%b
   print(suma,"\n",resta,"\n",multiplicacion,"\n",division,"\n",modulo)
except:
   print("Ha surgido un error")