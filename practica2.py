nombres = "hola mundo"
lista_nombre = ["ivan","luis"]


a = 1
b = 2 
if (a!=b):
    print("a y b son direfentes ")
elif (a <= b):
    print("a es menor que b")
else:
 print ( "estos numeros no entraron en la centencia ")

#for i in range(3):
#    print(i)


#texto = "hola mundo python este es mi "
#for i in texto:   
#    pass 
#contador_A=0
#if (a=="a" or a=="e"):
#   if (a=="a"):
#      contador_A = contador_A +1 

texto = "hola mundo python este es mi script "
cont_a=0
cont_e=0
cont_i=0
cont_o=0
cont_u=0

for i in texto:  
   if (i=="a" or i=="e"):
      if(i=="a"):
           cont_a += 1
           print("es una vocal")
   else:
      print("es una consonante")
for i in texto:  
   if (i=="e" or i=="e"):
      if(i=="e"):
           cont_e += 1
           print("es una vocal")
   else:
      print("es una consonante")
for i in texto:  
   if (i=="i" or i=="e"):
      if(i=="i"):
           cont_i += 1
           print("es una vocal")
   else:
      print("es una consonante")
for i in texto:  
   if (i=="o" or i=="e"):
      if(i=="o"):
           cont_o += 1
           print("es una vocal")
   else:
      print("es una consonante")
for i in texto:  
   if (i=="u" or i=="e"):
      if(i=="u"):
           cont_u += 1
           print("es una vocal")
   else:
      print("es una consonante")
print(f"la cantidad de la vocal a es {cont_a }")
print(f"la cantidad de la vocal e es {cont_e }")
print(f"la cantidad de la vocal i es {cont_i }")
print(f"la cantidad de la vocal o es {cont_o }")
print(f"la cantidad de la vocal u es {cont_u }")




