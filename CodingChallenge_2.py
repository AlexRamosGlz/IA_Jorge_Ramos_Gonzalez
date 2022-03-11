
#this functions takes 2 string and then return the 2 strings concatenated
def String101(message1, message2):

  #the parameter values will be stored in this var 
  completeMessage =  message1 + message2;

  #and then print it 
  print(completeMessage);

  #the phrase is declared inside the function 
  phrase = '"print()" se utiliza para imprimir valores en la consola.';

  #the same phrase will be the value returned from the function
  return phrase;

#this fella calls the functions and then prints the returned value
print(String101('Hello there!', "\nGeneral Kenoby!"));

