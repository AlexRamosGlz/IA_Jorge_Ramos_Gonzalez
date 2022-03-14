
#this function counts how many times the number 2 needs to be multiply bi itself to result into 1024
def counter(number):

  #counter initialized
  counter = 1;

  #this loop until the result is 1024
  while number < 1024:

    #the algorithm to get to 1024
     number = number * 2;

     #the counter indicates how many times it took to get 1024
     counter = counter + 1; 

  #returning the counter value
  return counter;

#printing the returned value 
print('se necesita multiplicar 2 por ',counter(2),' veces para llegar a 1024');