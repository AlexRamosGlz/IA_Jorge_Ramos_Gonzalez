
#thi function removes two elements
def removeFromList(lista): 

  #elements to remove
  lista.remove('amarillo');
  lista.remove('rojo');

  #returning the lista
  return lista;

#printing the returned value
print(removeFromList(['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']));