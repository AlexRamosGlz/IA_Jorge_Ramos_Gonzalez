
#this function formats the string given in the parameter
def stringFormater(name): 

  #the name var stores the name parameter and converts it to a title format
  name =  name.title();
  #then print it
  print(name);

  #this transforms the string into a lower case string
  toLowerCase = 'Esta Es Una Frase Para Ser Formateada'.lower();
  print(toLowerCase);

  #this transforms the string into a upper case string
  toUpperCase = 'Esta Es Una Frase Para Ser Formateada'.upper();
  print(toUpperCase);

  #in this case the function doesn't have to return a value
  return '';

#callig the stringFormater function with a string as a parameter
stringFormater('jorge ramos gonzalez');


