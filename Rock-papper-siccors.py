
import random 
import time

print('----------------------------------')
print('Camon Play Rock Papper or Siccors!')
print('----------------------------------')

jugador = int(input('''What do you choose?'
          1- Rock
          2- Papper       
          3- Siccors              
'''))

print('-----------------------')
print('Now is turn of the Bot!')
print('-----------------------')

choices = {1: 'Rock', 2: 'Paper', 3: 'Scissors'}
bot = random.randint(1,3)


for i in range(3,0,-1):
    time.sleep(1)
    print(i)

print(f'The bot choose: {choices[bot]}')

if jugador == bot:
    print("its a tie!")
elif (jugador == 1 and bot == 3) or (jugador == 2 and bot == 1) or (jugador == 3 and bot == 2):
    print("You win!")
else:
    print("You losed :( ")