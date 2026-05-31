import random
def guessit():
    num = random.randint(1,30)
    print('Hey i am thinking a number b/w 1 and 30 and you have to guess it.')

    for el in range(1,8):

        while True:
            MMN = input(f'move number {el}:')

        # Note: Try & Except statement on ValueError is a Good way to check whether an input contain digits or not other way is isdigit() method.
        # Read the 'How to do it when' notes for more info.
            try:
                num1 = int(MMN)
                MMM = num1
                break
            except ValueError:
                print('its not an integer')

        if MMM < num:
            print('Nope its too small, try again')
        elif MMM > num:
            print('Nope, its big')
        elif MMM == num:
            print('yup, you got it.')
            break
    print('no man you got it wrong')

        
guessit()


