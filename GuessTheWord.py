import random
# if you call list() on a string than every character of the string becomes an item of the list Ex: list('hello') => [h,e,l,l,o]

# Note that thisis the Code of 2 Project, 1st is GuessTheNumber, and the other is hangman game. 

litus = ['The','startswith','and','endswith','methods','return','True','if','the','string','value','they','are','called','on','begins','or','ends','respectively','with','the','string','passed','to','the','method','otherwise','they','return','False','Enter','the','following','into','the','inter','active','shell']
Thenumber = random.randint(0,len(litus)-1)

def GuessTheWord():
    myword = litus[Thenumber].lower()
    Elist = ['-'] * len(myword)
    Wlist = []
    dicti = {}
    count = 1
    
    for i, el in enumerate(myword):
        if el not in dicti:
            dicti[el.lower()] = []
        dicti[el.lower()].append(i) 
    
    for i in range(len(myword) * 2):
            while True:
                YY = (input(f'You have got {str(len(myword)*2)} attemps Go ahead, move number {count} :')).lower()
                if YY not in Wlist:
                   
                    if len(YY) != 1:
                        print('Nope the input needs to be single letter, Go again')
                    elif len(YY) == 1:
                        break
                
                elif YY in Wlist:
                     print('You are guessing it wrong again!')
           
            if YY in myword and YY in dicti:
                print('Yep this character is in the word')
                
                if len(dicti[YY]) != 1:
                    Aw = dicti[YY][0]
                    Elist[Aw] = YY
                    del dicti[YY][0]
                    print(''.join(Elist))

                    if len(Wlist) > 0:
                        print('Your wrong guesses: '+','.join(Wlist))

                elif len(dicti[YY]) == 1:
                    Aw = dicti[YY][0]
                    Elist[Aw] = YY
                    del dicti[YY]
                    print(''.join(Elist))

                    if len(Wlist) > 0:
                        print('Your wrong guesses: '+','.join(Wlist))

            elif YY not in myword:
                print('Nope its not in the myword')
                print(''.join(Elist))
                Wlist.append(YY)
                print('Your wrong guesses: '+','.join(Wlist))

            elif YY in myword and YY not in dicti:
                print('it was there but Sorry that letter does not exist anymore, so for precaution i am now adding it Elist, it wont burn your move')
                Wlist.append(YY)
                print(''.join(Elist))

                if len(Wlist) > 0:
                    print('Your wrong guess: '+','.join(Wlist))

            if '-' not in Elist:
                print()
                print('Yup you got it right!')
                return
            count += 1

    print('alright so after all, these are the characters that you have correctly guessed')
    
    print(''.join(Elist))
    DE = input('now tell me whats the word: ')

    if DE == myword:
        print('you got it right')
    else:
        print(f'Nope you lost the game, the word is {myword}')

#GuessTheWord()






# It's a Chatgpt's solution:
# Main mistakes: overcomplicated logic, unnecessary conditions, wrong loop structure earlier, and not using simple patterns for updates.
import random
litus = ['the','startswith','and','endswith','methods','return','true','if','the','string','value','they','are','called','on','begins','or','ends','respectively','with','the','string','passed','to','the','method','otherwise','they','return','false','enter','the','following','into','the','inter','active','shell']

def hangman():
    # Choice is a function from random Module, that simply picks a random element from any sequenced data type (lists, tuple and strings) but not sets
    myword = random.choice(litus)
    Elist = ['-'] * len(myword)
    # From here we can see that, if we multiply a list by a number(n) than it crates n number of lists and adds all of them together in an order to form one big list. Ex: [1,2]*2 => [1,2,1,2]
    
    # Here in this variable we have created a set. We can not put parentheses to make set b/c that will create a tuple. Read pdf for more.
    guessed = set() 
    wrong = []
    lives = 6

    dicti = {}
    for i, ch in enumerate(myword):
        # setdefault is a dictionary method that either gets the value of the key if exists, and if it does not, it creates that key with default value and than returns that value.
        dicti.setdefault(ch, []).append(i)   

    print(f"Guess the word! It has {len(myword)} letters")

    while lives > 0:
        print("Word:", ' '.join(Elist))
        print("Wrong guesses:", ','.join(wrong))
        print("Lives left:", lives)

        guess = input("Enter a letter: ").lower()

        if len(guess) != 1:
            print("Enter only one letter")
            continue

        if guess in guessed:
            print("You already guessed that")
            continue

        guessed.add(guess)

        if guess in dicti:
            print("Correct!")
            for idx in dicti[guess]:  # Basically, if you guess a letter correctly than all the instances of that letter is revealed. 
                Elist[idx] = guess
            del dicti[guess]
        else:
            print("Wrong!")
            lives -= 1
            wrong.append(guess)

        if '-' not in Elist:
            print("You won! The word was:", myword)
            return

    print("You lost! The word was:", myword)

hangman()
