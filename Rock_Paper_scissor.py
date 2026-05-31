import random
# Avoid the redunduncy
def RPS(): 
    DICT = {'user' : 0, 'pc' : 0}
    A = 1
    mylist = ['rock', 'paper', 'scissor']
    print('lets play rock paper scissor:')
    print('The game will be 5 rounds and the player who wins the most rounds will win')

    while A < 6:
        AA = input(f'Play your move # {A}:(Rock-Paper-Scissor) ').lower()
        if AA not in ['rock', 'paper', 'scissor']:
            print('Move is invalid try again')
            continue
        
        if AA in ['rock', 'paper', 'scissor']:
            AB = random.choice([random.choice(mylist), random.choice(mylist), random.choice(mylist)])
            if AA == 'rock' and  AB == 'rock':
                print()
                print(f'OOPS its a draw! Because we both said {AA}')
                A += 1
                print(f'Current score: You({str(DICT['user'])}) - PC({str(DICT['pc'])})')
            elif AA == 'rock' and  AB == 'scissor':
                print()
                print(f'Hey You said {AA} i said {AB} so you won')                          # Avoid the redunduncy
                A += 1
                DICT['user'] = DICT['user'] + 1
                print(f'Current score: You({str(DICT['user'])}) - PC({str(DICT['pc'])})')
            elif AA == 'rock' and  AB == 'paper':
                print()
                print(f'Hey You said {AA} i said {AB} so I won')
                A += 1
                DICT['pc'] = DICT['pc'] + 1
                print(f'Current score: You({str(DICT['user'])}) - PC({str(DICT['pc'])})')
            elif AA == 'paper' and  AB == 'scissor':
                print()
                print(f'Hey You said {AA} i said {AB} so I won')
                A += 1
                DICT['pc'] = DICT['pc'] + 1
                print(f'Current score: You({str(DICT['user'])}) - PC({str(DICT['pc'])})')
            elif AA == 'paper' and  AB == 'rock':
                print()
                print(f'Hey You said {AA} i said {AB} so you won')
                A += 1
                DICT['user'] = DICT['user'] + 1
                print(f'Current score: You({str(DICT['user'])}) - PC({str(DICT['pc'])})')
            elif AA == 'paper' and  AB == 'paper':
                print()
                print(f'OOPS its a draw! Because we both said {AA}')
                A += 1
                print(f'Current score: You({str(DICT['user'])}) - PC({str(DICT['pc'])})')
            elif AA == 'scissor' and  AB == 'paper':
                print()
                print(f'Hey You said {AA} i said {AB} so you won')
                A += 1
                DICT['user'] = DICT['user'] + 1
                print(f'Current score: You({str(DICT['user'])}) - PC({str(DICT['pc'])})')
            elif AA == 'scissor' and  AB == 'rock':
                print()
                print(f'Hey You said {AA} i said {AB} so I won')
                A += 1
                DICT['pc'] = DICT['pc'] + 1
                print(f'Current score: You({str(DICT['user'])}) - PC({str(DICT['pc'])})')
            elif AA == 'scissor' and  AB == 'scissor':
                print()
                print(f'OOPS its a draw! Because we both said {AA}')
                A += 1
                print(f'Current score: You({str(DICT['user'])}) - PC({str(DICT['pc'])})')

    if DICT['user'] > DICT['pc']:
        print(f'Congrats You won! {DICT['user']}-{DICT['pc']}')
        return
    elif DICT['user'] == DICT['pc']:
        print(f'its a draw! {DICT['user']}-{DICT['pc']}')
        return
    print(f'sorry you loss the game {DICT['pc']}-{DICT['user']}')

RPS()
            

# Chatgpt's version of ROCK_PAPER_SCISSOR:
# Chatgpt justs removed the redundancy in condional statements and used multiline syntax for easing readability:
import random
def RPS_():
    score = {'user': 0, 'pc': 0}
    choices = ['rock', 'paper', 'scissor']
    
    print('Lets play Rock Paper Scissor!')
    print('Best of 5 rounds wins.')
    round_num = 1

    while round_num <= 5:
        user_choice = input(f'Round {round_num} - Your move (rock/paper/scissor): ').lower()

        if user_choice not in choices:
            print('Invalid move, try again.')
            continue

        pc_choice = random.choice(choices)
        print(f'PC chose: {pc_choice}')

        if user_choice == pc_choice:
            print("It's a draw!")
        elif (user_choice == 'rock' and pc_choice == 'scissor') or \
(user_choice == \
 'paper' and pc_choice == 'rock') or \
(user_choice == 'scissor' and pc_choice == 'paper'):   # Read line # 126
            print('You win this round!')
            score['user'] += 1
        else:
            print('PC wins this round!')
            score['pc'] += 1

        print(f"Score: You({score['user']}) - PC({score['pc']})")
        round_num += 1

    print('Final Result:')
    if score['user'] > score['pc']:
        print(f"You won the game! {score['user']} - {score['pc']}")
    elif score['user'] < score['pc']:
        print(f"You lost the game! {score['pc']} - {score['user']}")
    else:
        print(f"It's a draw! {score['user']} - {score['pc']}")

RPS_()

    
# If there is a very big line and you want to write that big line into multiple lines that you can use '\' and '()' for that READ PDF.


#    elif (user_choice == 'rock' and pc_choice == 'scissor') or (user_choice == 'paper' and pc_choice == 'rock') or (user_choice == 'scissor' and pc_choice == 'paper'):   # 

#    elif (user_choice == 'rock' and pc_choice == 'scissor') or \                         All these 3 block of code works the same, just by using
#    (user_choice == 'paper' and pc_choice == 'rock') or \                                '\' and '()' we converted it multiple lines
#    (user_choice == 'scissor' and pc_choice == 'paper'):   


#    if ((user_choice == 'rock' and pc_choice == 'scissor') or 
#    (user_choice == 'paper' and pc_choice == 'rock') or 
#    (user_choice == 'scissor' and pc_choice == 'paper')):   
           