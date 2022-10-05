"""Guess the number game
Computer guesses the number by itself"""

import numpy as np

def random_predict(number:int=1) -> int:
    """Random number guessing

    Args:
        number (int, optional): The number we need to guess. Defaults to 1.

    Returns:
        int: Number of tries
    """
    count = 0
    
    while True:
        count += 1
        predict_number = np.random.randint(1, 101) #predicting number
        if number == predict_number:
            break #exit the cycle when guessed
    return (count)

def score_game(random_predict) -> int:
    """What is the mean value of tries for 1000 tries guess our algorithm

    Args:
        random_predict (_type_): guessing function

    Returns:
        int: mean value of tries
    """
    count_ls = [] #the list to store the number of tries
    np.random.seed(1) #fixing the seed
    random_array = np.random.randint(1, 101, size=(1000)) #random number list
    
    for number in random_array:
        count_ls.append(random_predict(number))
        
    score = int(np.mean(count_ls)) #mean value of tries
    
    print(f"Your algorithm guesses the number in mean tries of: {score} tries")

#RUN
if __name__ == '__main__':
    score_game(random_predict)
