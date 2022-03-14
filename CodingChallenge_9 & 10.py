
#this functions gets a certain index in the list
def getPosition(list):

  #printing the element in the index 3 of the list
  print('the element in the index 3 is: ',list[3]);

  #printing the index of the element 'rojo'
  print('the index of the element "rojo" is: ',list.index('rojo'));

  #printing the index of the element 'rosa'
  print('the index of the element "rosa" is: ',list.index('rosa'));

  #prints the negative indexs of the given elements
  print('the negative index of the element "naranja" is: ', list.index('naranja') - 10);
  print('the negative index of the element "amarillo" is: ', list.index('amarillo') - 10);
  print('the negative index of the element "lila" is: ', list.index('lila') - 10);
  print('the negative index of the element "blanco" is: ', list.index('blanco') - 10);
  print('the negative index of the element "rojo" is: ', list.index('rojo') - 10);

  
  #returning a new list
  return ['tres', 'dos', 'cinco', 'cuatro', 'uno'];


#calling the function
getPosition(['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']);