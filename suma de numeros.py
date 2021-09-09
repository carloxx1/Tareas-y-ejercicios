def sumadenumeros(numeros):

   if len(numeros) == 1:
        return numeros[0]
   else:
        return numeros[0] + sumadenumeros(numeros[1:])
lista=[2,3,4,1,5]
resultado= sumadenumeros(lista)
print(resultado)
