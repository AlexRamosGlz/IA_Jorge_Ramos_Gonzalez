
def ageFilter(age):

  if age <= 0:
    print('Nadie puede tener esa edad.')
  
  elif age <= 1 and age < 18:
    print('Eres menor de edad.')
  
  elif age <= 100:
    print('Eres mayor de edad.')

  else:
    print('Edad no válida.')

ageFilter(int(input('Cual es tu edad ?\n')))
