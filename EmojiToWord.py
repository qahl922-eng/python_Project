# This Project help us to study Emojis.
import  demoji, emoji
text = "These are my emojis: 😜😂😭👋⭐⭐💛💚💝"
texto = 'These are my emojis: :winking_face_with_tongue: :face_with_tears_of_joy: :loudly_crying_face: :waving_hand: :star: :star: :yellow_heart: :green_heart: :heart_with_ribbon:'
# This Function returns the dictionary of all the unique emojis as keys and thier description as values. 
pattern = demoji.findall(text)
print(pattern)

# This Function gives you the list of all the (emoji) / (descriptions of all emoji). 
# If you pass nothing / True as 2nd argunent, you will get list of description. if False is passed, you will get list of emoji.
print(demoji.findall_list(text, desc = False))
print(demoji.findall_list(text))                # This Func even returns emojis that occurs more than once in text.

# This function replaces every emoji with the string you pass in 2nd argument.
# if 2nd argument is'nt pass, it will replace all emoji with empty strings. Basically removing all the emojis.
print(demoji.replace(text, repl = '... '))

# This Func replace emoji with it's Description and put the substring you pass in as 2nd arg on both side of descriptiion. 
print(demoji.replace_with_desc(text, sep = ', '))

# This function converts emoji into there description and place items of the tuples that you pass as 2nd arg around them.
print(emoji.demojize(text, delimiters = (':',':')))

# This func takes string and convert the 'emoji discription' surrounded by delimiters inside the string to emojis.
print(emoji.emojize(texto,language ='en', delimiters = (':',':')))

# This Func takes in single character and tells you whether it is an emoji or not, by True or False. if > 1 character, also returns false. 
print(emoji.is_emoji('💚'))

# This function returns the list of unique emoji's only but in a random order.
print(emoji.distinct_emoji_list(text))

# This function returns the position and description of all the emojis, as a ORDERED list of dictionary.
# Each dictionary consists of 3 key:value pair, 2 of positions and one emoji:(description), key value pair.
print(emoji.emoji_list(text))

# This function works the same as replace() function of demoji library.
print(emoji.replace_emoji(text, replace = '.[].'))