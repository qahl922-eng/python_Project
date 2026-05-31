import random

def Num21():
    count = 0
    print('lets play 21-Number game:')
    print('So the rules are that we can say 1-3 numbers at a time on our turn')
    print('But the one who say number 21. he will loose, so try to avoid number 21')

    # choose 1st player
    while True:
        gamer = input('Tell me who should go 1st, user or PC: ').lower()
        if gamer == 'user' or gamer == 'pc':
            turner = gamer
            break
        else:
            print('sorry you say eiether user or pc')

    while True:
        if turner == 'user':   # player move  line (19-38)
            print(f'current count is: {count}')
            try:
                AA = int(input('ok so what number you wanna say: '))
            except ValueError:
                print('sorry the input is invalid.')
                continue

            if AA in [1,2,3]:
                listr = []
                for el in range(num):
                    count += 1
                    listr.append(str(count))
                print(','.join(listr))
                turner = 'pc'
                user_last_input = AA

            elif AA > 3 or AA < 1:    # invalid move check
                print('OOPs, number is greater than 3. try agin!')
                continue

        elif turner == 'pc':  # PC's turn line (40-53)
            if count == 0:
                count += int(random.choice('123'))
                print(count)
                turner = 'user'
            else:
                num = 4 - user_last_input            
                lists = []
                print('ok so now its my turn')
                for el in range(num):
                    count += 1
                    lists.append(str(count))
                print(','.join(lists))
                turner = 'user'


                    
        if count >= 21:  # winner check
            print('we have a winner here!')
            if turner == 'pc':
                print('You said 21. PC wins this game, sorry you loose.')
            else:
                print('PC siad 21. Congrats Man! You Won.')
            break

#Num21()


import random      # By Chatgpt
# Perfect AI: always tries to land on 5, 9, 13, 17 (forcing you to hit 21)

def Num215():
    count = 0
    print('Lets play 21-Number game!')
    print('Say 1–3 numbers each turn. Whoever says 21 loses.')

    # choose first player
    while True:
        turner = input('Who goes first (user/pc): ').lower()
        if turner in ['user', 'pc']:
            break
        print('Invalid input.')

    while True:
        if turner == 'user':
            print(f'Current number: {count}')
            try:
                move = int(input('How many numbers you want to say (1-3): '))
            except ValueError:
                print('Invalid input.')
                continue

            if move not in [1, 2, 3]:
                print('Only 1, 2 or 3 allowed.')
                continue

            said = []
            for _ in range(move):
                count += 1
                said.append(str(count))
            print(','.join(said))

            # check loss
            if count >= 21:
                print('You said 21 → You lose!')
                break

            turner = 'pc'

        else:  # PC turn
            print('PC turn...')

            # Perfect move: This is the brain of the game. see line # 134.
            target = ((count // 4) + 1) * 4 + 1
            move = target - count

            if move < 1 or move > 3:
                move = random.randint(1, 3)

            said = []
            for _ in range(move):
                count += 1
                said.append(str(count))
            print(','.join(said))

            # check loss
            if count >= 21:
                print('PC said 21 → PC loses!')
                break

            turner = 'user'

Num215()

# PC wnats to land on these numbers : 5, 9, 13, 17. Because from here pc can force you to say 21.
# Target = ((count // 4) + 1) * 4 + 1 =>      this line finds the next safe number (5, 9, 13, 17).
# move = target - count =>       this line finds the number that will take you to the safe number.
# code on line (116-117) take care of any invalid attemps and gives a random number between 1-3.
 