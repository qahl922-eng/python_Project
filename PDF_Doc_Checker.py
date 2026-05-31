# # One of the most Depressing and difficult days 12-15 aprils, Because of confusions.
# import hashlib
# import os
# # Read the Hashing pdfs.

# def hasher(file_path):
#     '''This function generate hashes of files passed in using sha256()'''

#     hash_obj = hashlib.sha256()

#     try:
#         with open(f"{file_path}", 'rb') as f:
#             while True:
#                 chunk = f.read(4096)
#                 if not chunk:
#                     break
#                 hash_obj.update(chunk)

#     except Exception as e:
#         print(f'file was not hashed because of Error:{e}')
#         return None
    
#     return hash_obj.hexdigest()

# def file_comp(path1, path2):

#     # File authentications
#     if not os.path.isfile(path1):
#         print(f'Error {path1} does not exists')
#         return 
#     if not os.path.isfile(path2):
#         print(f'Error {path2} does not exists')
#         return 
#     # Extension cheker for pdfs
#     if not path1.lower().endswith('.pdf') or not path1.lower().endswith('.pdf'):
#         print('one or both of the file is not a pdf, they must be pdfs')
#         return

#     # Creating hashes of files
#     hash1 = hasher(path1)
#     hash2 = hasher(path2)

#     if hash1 == None or hash2 == None:
#         print('cant compare the odfs due to read Errror')
#         return
#     # Comparisons:
#     if hash1 == hash2:
#         print('Both the pdfs are identical')
#     else:
#         print('PDFS are not identical they are different')


# paths1 = "C:\\Users\\PMLS\\Documents\\automatetheboringstuffwithpython_new_113151.pdf"
# paths2 = "C:\\Users\\PMLS\\Documents\\automatetheboringstuffwithpython_new_113151.pdf"

# file_comp(paths1, paths2)

# hashe = hashlib.sha256()
# A = 'Hello'
# hashe.update(A.encode())
# print(hashe.digest())
# print(hashe.hexdigest())
# hashes = hashlib.sha256()
# with open("C:\\Users\\PMLS\\Documents\\automatetheboringstuffwithpython_new_113151.pdf", 'rb') as xe:
#     while True:
#         chunker = xe.read(1024)
#         if not chunker:
#             break
#         hashes.update(chunker)
#     print(hashes.hexdigest())


# # Password checker:
# def password():

#     hasho = hashlib.sha256()
#     A = 'tonoplast'
#     hasho.update(A.encode())
#     myhash = hasho.hexdigest()

#     names = {'owais' : myhash }
#     if (user_ := input("What's your name please: ")) in names:    # Walrus operator ':=' used here for the 1st time.
#         print('Yes your name is in the users')
#         passw = input("what's your password: ")

#         hashoi = hashlib.sha256()
#         hashoi.update(passw.encode())
#         myhash = hashoi.hexdigest()

#         if myhash == names['owais']:
#             print('Password correct, Your are logged in.')
#         else:
#             print('Nope, Wrog password!!')

#     else:
#         print('Nope i have not find your name.')

# password()
import pprint
A = {29393:29202, 'hello': 34334, 'dog': 89}
pprint.pprint(A)
AC =[A,'B',['hello',[A,3455,[A]]]]
Z=pprint.pformat(AC)
print(Z)      

