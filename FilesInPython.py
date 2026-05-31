# Practice on files in Python:
import os
AB = str(os.path.join('hello', 'killme','okk'))
print(AB)  # The output of this line is  ' hello\killme\okk '

print(os.getcwd()) # it will returns you back the current working directery in which your program is operating in.
print(os.chdir('C:\\Users\\PMLS\\AppData\\Local\\Programs\\Microsoft VS Code')) 
# os.chdir() changes the directory from where your program is operating. Read files in python pdf for more.
print(os.getcwd())
#print(os.chdir('..\\'))  # This (..\\) is a relative path and it means the parent folder of the current directory. 
print(os.listdir('.\\')) # (.\\) means the current working directory and its optional because python takes  in 'cwd' as destiny if nothing was given.
print(os.listdir())      # listdir() function will list out all the files and folders in the cwd. looking at it you can see that (.\\) is optional.
                         # see above, we have not passed anything to listdir() but still it lists out files & folders of because .\\ is compeletly optional. 
                         # it means if you wont provide the path to the function is os module, so it will take path of cwd by default.

# This os.makedirs() function makes new directories and it takes in 2 argument, path of the dirctory that you are making. it goes onto that provided
# path and creates whatever is missing and the 2nd argument ('exist_ok=True') prevents FileExistError that comes if only the last file/folder already exists.
print(os.makedirs('C:\\Users\\PMLS\\AppData\\Local\\google\\Demis\\dows.txt', exist_ok=True))
#os.chdir('C:\\Users\\PMLS\\AppData\\Local\\google\\Demis')
print(os.getcwd())
print(os.path.abspath('..\\fucky\\rusty\\..\\dick')) 
 # This function converts relative to abspath and returns you back. Read the pdf for how relative path works?
print(os.path.isabs('C:\\Users\\PMLS\\AppData\\Local')) # This method tells you whether a path is absolute or not. just check 'C:\\' at the start.
print(os.path.relpath(path='C:\\Users'))
 # relpath() Takes 2 arguments(path,start): 1st, where you wanna go. 2nd argument is optional, but its from where you wanna go, if not given it takes cwd as 2nd Arg. 
 # ths function returns relative path between path and start location.
print(os.path.dirname('C:\\Users\\PMLS\\AppData\\Local\\google\\Demis'))
print(os.path.basename('C:\\Users\\PMLS\\AppData\\Local\\google\\Demis'))
print('C:\\Users\\PMLS\\AppData\\Local\\google\\Demis'.split(os.path.sep)) 
 # (split is a string method that seperate the string on its left and os.path.sep is an attribute that gives off '\\') separate text on '\\'
#  print(os.path.getsize()) this method gives you the size of files in bytes
print(os.getcwd())
file = open('file98.txt','w')
file.write('Hello my dear AI How are you.')
file.close()
file1 = open('file98.txt','a')
file1.write('\n This must give us a second line')
file1.close()
AA = open('file98.txt','r')
print(AA.readlines()) # it gives you the list of all the lines inside the file, basically it searches the whole text and where it finds \n it creates an item
print(AA.read())
