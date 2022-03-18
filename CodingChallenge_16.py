
#tupla:  tuplas are almost the same as list, but inmutables and also declared with () instead of []

#this functions takes a tupla and make some operations with it
def tupla(tupla):

  #printing the value in the position 2
  print(tupla[2])

  #declaring a new tupla with some numbers in it 
  numeros = (10, 5, 1, 11)

  #returning a simple ecuation that gives a 25 as result
  return (numeros[3] - numeros[2]) + (numeros[0] + numeros[1])

#printing the returned value
print('The result is: ', tupla(('rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja')))