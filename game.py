"""Game guess the number"""

import numpy as np

number = np.random.randint(1, 101) #make a random number

#try count
count = 0

while True:
    count += 1
    predict_number = int(input('Guess the number from 1 to 100: '))
    
    if predict_number > number:
        print('The number is smaller.')
        
    elif predict_number < number:
        print('The number is bigger')
        
    else:
        print(f'You guessed the number: the number is {number}, you used {count} tries.')
        break #We exit the cycle