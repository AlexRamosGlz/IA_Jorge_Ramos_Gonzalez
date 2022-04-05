import random


a = [0, 0, 0, 0, 0]
b = [0, 0, 0, 0, 0]
c = [0, 0, 0, 0, 0]
d = [0, 0, 0, 0, 0]
e = [0, 0, 0, 0, 0]

infitte = [a, b, c, d, e, 1,1,1,1,1,1,1,1,1,1,11,1,1,1,1,1,1,1,]

stop = False
counter = 0
todos = []
top5 = []
primero = []
segundo = []

def race(list):
  global stop 
  i = 0
  if counter < 5:
    while i < 5:
      list[i] = random.uniform(1, 20).__round__(1) #km /hr
      todos.append(list[i])
      i += 1

    list.sort()

  if counter == 5:
    i = -5
    todos.sort()
    print('\ntodos: ', todos)
    while i < 0:
      top5.append(todos[i])
      i += 1
    print('\ntop5: ', top5)

    primero = top5[-1]
    print('\nPrimer Lugar: ', primero)

  if counter == 6:
    todos.pop(-1)
    segundo = todos[-1]
    print('\nSegundo: ', segundo)
    stop = not stop

  return 1

 
while(stop == False):
  counter += race(infitte)

print('\nSe nececistan minimo: ', counter, 'carreras')


