
#this function appensd the elements given
def appendElement(elements):

  #lista is the list in which we want to append the elements
  lista = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja'];

  #this loops the elements given and append them in the lista list
  for el in elements:
    lista.append(el);

  #returning the lista
  return lista;

#ptrinting the lista
print('Elements Appended: ', appendElement(['fuxia', 'celeste']));


#this function inserts the elements
def insertElements():
  
  #lista is the list in which we want to insert the elements
  lista = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja'];
  
  #inserting the elements in the lista
  lista.insert(-2, 'turquesa');
  lista.insert(-5, 'magenta');

  #returning the lista
  return lista;

#printing the returned value
print('Elements Inserted: ', insertElements());

