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
for i in texto:  
   if (i=="a" or i=="e"):
      if(i=="a"):
           cont_a += 1
           print("es una vocal")
   elif(i==" "):
     print("es un espacio")
   else:
      print("es una consonante")
print(f"la cantidad de la vocal a es {cont_a }")




