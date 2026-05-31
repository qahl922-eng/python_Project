'''Problem # 1: Contains Duplicate II: You are given an integer array nums and an integer k. Your task is to determine
                whether there are two equal values in the array such that the distance between their indices is at most
                k. In simple words, you need to check whether the same number appears again nearby within k positions.'''
# Although its my solution apart from the commented line, But almost the whole concept is introduced and helped calibirate by ChatGPT.
def Duplicate_II(nums, k):
    
    hashset = set()

    for i,num in enumerate(nums):

        if num in hashset:
            return True
        hashset.add(num)

        if i >= k:        # in my original solution i used just '>' but chatGPT suggested '>='
            hashset.remove(nums[i-k])

    return False

'''Timme Complexity: O(n)  Space Complexity: O(k)
 because the HashSet stores at most k elements at any time.'''

'''Problem # 2: Find All Duplicates in an Array: You are given an integer array nums where some elements appear twice
                and others appear once. Your task is to return all numbers that appear exactly twice. In simple words, 
                instead of only checking whether duplicates exist, now you must collect all duplicate values.'''
# This solution is done by myself, without any help from chatgpt, just one typo was a mistake.

def AllDuplicates(nums):

    res = []
    hashset = set()

    for el in nums:

        if el in hashset:
            if el not in res:
                res.append(el)
            
        hashset.add(el)

    return res

'''Timme Complexity: O(n)  Space Complexity: O(n)'''

'''Problem # 3: Intersection of Two Arrays: You are given two integer arrays nums1 and nums2. Your task is to return an array 
                containing all unique elements that appear in both arrays. In simple words, find the common values shared by 
                both arrays, but include each value only once.'''
# This solution is done by myself, without any help from chatgpt.

def intersect(nums1, nums2):
    
    hashset1 = set()

    res = []

    for el in nums1:
        hashset1.add(el)

    for el in nums2:
        if el in hashset1 and el not in res:
            res.append(el)

    return res

'''Time Complexity: O(n + m)   Space Complexity: O(n)'''

'''Problem # 4: Happy Number: A number is called a “happy number” if by repeatedly replacing the number with the sum of the
                squares of its digits, you eventually reach 1. If the process enters an endless cycle and never reaches 1, 
                then the number is not happy. Your task is to return True if a number is happy, otherwise return False. '''
# with Error detection from chatGPT, I solved this on my own, with one little logical error, see comments.

def happynum(num):

    if num == 1:
        return True

    check = num
    hashset = set()
    
    while check != 1:
        tt = 0
        for n in str(check):
            tt += int(n)**2

        if tt in hashset:     # logical Error was this check loop, it was at the end, just right after when i add() tt in hashset.
            return False      # That means every time i check 'tt in hashset' after adding tt in hashset, which always returns False.

        if tt == 1:
            return True
        else:
            check = tt
            hashset.add(tt)

                             # Here was the check loop

'''Time Complexity: O(log n)      Space Complexity: O(log n)'''

'''Problem # 5: Isomorphic Strings: Given two strings s and t, determine whether they are isomorphic. Two strings are isomorphic 
                if characters in s can be replaced to get t, while preserving the order of characters. Each character must map to 
                exactly one other character, and no two different characters may map to the same character.'''
# Although by Error detection from chatGPT, this is my own solution, specially last check via hashset logic.

def Isomorph(s, t):

    if len(s) != len(t):
        return False
            
    hashmap = {}               # s_elements will be key, t_elements will be values.

    for i in range(len(s)):

        if s[i] in hashmap and t[i] != hashmap[s[i]]:
            return False

        hashmap[s[i]] = t[i]

    hashset = set()

    for el in hashmap.values():    # This Hashset Logic is solely mine.
        if el in hashset:
            return False
        hashset.add(el)
  
    return True

'''Time Complexity: O(n)                                  Space Complexity: O(n)'''



