# Problem # 1: Return True if an array contain Dupliicates and return false, if it does not.

def Duplicate(nums):

    set_ = set()

    for el in nums:
        if el in set_:
            return True
        else:
            set_.add(el)   # we searched this method .add() on google.
    return False

# Space Complexity = O(n),       Time complexity = O(n)

# Problem # 2: You are given two strings s and t. Return True if t is an anagram of s, otherwise return False.
# An anagram means both strings contain the same characters with the same frequencies, just possibly in different orders.
# Ex: listen & silent are anagram.

def Anagram(S, T):

    s = S.lower()
    t = T.lower()

    if len(s) != len(t):       # This if statment was suggested by Chatgpt
        return False

    Hash = {}

    for el in s:
        if el not in Hash:
            Hash[el] = 1
        elif el in Hash:
            Hash[el] += 1
    
    for el in t:
        if el not in Hash:      # This if statment was suggested by Chatgpt b/c i got a keyerror on the next if statment.
            return False
        if Hash[el] == 1:       # I was getting keyerror b/c i accessed Hash[el] value without checking whether it's present in Hash / not.
            del Hash[el]        # you get keyerror if you access that key ina hashmap, that does not exist.
        else:                   # Here instead of else we were using 'elif el in Hash' which is redundant b/c 1st if already checks that.
            Hash[el] -= 1       # B/c if the program execution escaped 1st if & reached here than that means, el exists in Hash.

    # initially we were using 'Hash.keys()' instead of just 'Hash' which just check whether Hash is empty or not, if it's, it just return True.
    if not Hash:                # we had not added the else statment at 1st, and b/c of that we got None in return. 
        return True             # B/c the above if statement returns True only if the Hash is empty.
    else:
        return False
#   return len(Hash) == 0       #  This one line is enough for returning True or False and can replace these if : else block above.

#   Space Complexity = O(n),       Time complexity = O(n)


# Problem # 3: Given two integer arrays nums1 and nums2, return an array containing their unique common elements. Order can be any.

def intersect(num1, num2):

    nums =  []
    set_ = set()

    for el in num1:
        if el not in set_:
            set_.add(el)

    for el in num2:
        if el in set_:
            nums.append(el)
            set_.remove(el)   # just this remove method was the one i seen from outside.
                              # on Chatgpt's suggession, b/c we have to return only unique common elements.
    return nums

#   Space Complexity = O(n),       Time complexity = O(n)

# Problem # 4:   Given an array of strings strs, group all the anagrams together. You can return the groups in any order.
# I absolutley failed at this & its a chatgpt's Solution.

def Anagrams(strings):

    Hash_map = {}
    for str in strings:

        Key = tuple(sorted(str))

        if Key not in Hash_map:
            Hash_map[Key] = []

        Hash_map[Key].append(str)

    return list(Hash_map.values())  # Note: Values() method of Dictionary returns a VIEW OBJECT of the type dict_values, not a list.
    
# Time Complexity: O(n * k log k)   Space Complexity: O(n * k)              n = number of strings  k = average length of each string'

# Problem # 4: Given an integer array nums and an integer k, return the k most frequent elements, You may return the answer in any order.
# This is My own solution.

def Frequency(intergers,K):

    Hash_map = {}
    FinalList = []

    for el in intergers:
        if el not in Hash_map:
            Hash_map[el] = 1
        elif el in Hash_map:
            Hash_map[el] += 1

    Lista = []
    for k, v in Hash_map.items():
        Lista.append((v,k))
    
    Lista.sort(reverse=True)
    for el in range(K):
        FinalList.append(Lista[el][1])

    return FinalList

# Time Complexity: O(n logn).          Space Complexity: O(n)

