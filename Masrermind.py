'''Mastermind Game: its a multiplayer game in which you have to guess an n digit long number and the player who 
                    guessed the number in least turns wins'''

def mastermind():
    import random

    num = str(random.randrange(1000, 10000))

    while True:
            try:
                n = input(f'Guess a 4 digits long number:                             ')
                A = int(n)
        
            except ValueError:
                print('I am Sorry you can only Pass numeric Values')
                continue

            if len(n) == 4:
                break
            print('Sorry you can pass only 4 digit number')

    if num == int(n):
        print('WoW, You guessed the number in your 1st try! \nSo You are a Mastermind.\nDo you wanna play it again')
        return
    
    count = 0

    while True:

        count += 1
        
        if num == n:
            print(f'Yes You Did it.\nYou Guessed the number in {str(count)} turns.')
            return

        correct = ['X'] * 4

        ctr = 0 
        for el in range(4):

            if n[el] == num[el]:
                correct[el] = n[el]
            else:
                ctr += 1
        
        if ctr == 4:
            print('Nope, You have not Guessed Even a single digit Correctly')

        else:
            print('You have Guessed Some of the Digit correcly and here they are:')
            for el in correct: print(el, end=' ')
            print()
            
        while True:

            try:
                n = input(f'So You have Tryed {str(count)} Times, Whats Your next Guess:         ')
                B = str(n)
                
                if B == 'q':
                    print('i am sorry you are unable to guess the number successfully, and the number is', num)
                    return
        
            except ValueError:
                print('I am Sorry you can only Pass numeric Values')
                continue

            if len(n) == 4:
                break
            print('Sorry you can pass only 4 digits long number')

            
mastermind()






    

