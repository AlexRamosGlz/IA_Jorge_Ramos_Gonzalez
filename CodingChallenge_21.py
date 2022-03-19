
#check if contains a certain string
def checkIfContains(tuple): 

  #if rojo then print else don't
  if 'rojo' in tuple:
    print('El color rojo está admitido')
  else:
    print('Color no admitido')
  
checkIfContains(('rojo', 'verde', 'morado', 'negro'))