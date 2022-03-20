
#declaring the 1st dictionary 
teclado_1 = {
  'Categorias': 'Teclados',
  'Modelo': 'Hyper Allows FPS pro',
  'Precio': '89.99'
}

#declaring the 2nd dictionary
teclado_2 = {
	'Categoría': 'Teclados',
	'Modelo': 'Corsair K55 RGB',
	'Precio': '59.99'
}

#deleting the 1st dictionary
del teclado_1

#deleting the 'categoria' field from the second dictionary
del teclado_2['Categoría']

#deleting the 'precio' field from the second dictionary
del teclado_2['Precio']

#printing the 'Modelo' field from the second dictionary
print(teclado_2['Modelo'])



