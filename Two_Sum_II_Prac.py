''' Problem # 1: Container With Most Water.
                 You are given an integer array height where each element represents the height of a vertical line. 
                 Choose two lines such that together with the x-axis they form a container that holds the maximum 
                 amount of water. Return the maximum amount of water the container can store.'''

def MostWater(height):

    right = len(height) - 1
    left = 0

    Maxarea = 0
    
    while left < right:
        area = (right - left) * min(height[left], height[right])

        if area > Maxarea:
              Maxarea =  area
        if height[left] < height[right]:
             left += 1
        else:
             right -= 1

    return Maxarea
''' time complexity is O(n)        space complexity is O(1) '''

''' Problem # 2 — Valid Palindrome. Given a string s, return True if it is a palindrome, otherwise return False.'''

def ispalindrome(S):

    s = S.lower() 
    left =  0
    right = len(s) - 1

    while left < right:
        if not s[left].isalnum():   # This method was seen through google search.
            left += 1
        elif not s[right].isalnum():  # It return True if the Character is integer or Alphabet and false otherwise(special Characters).
            right -= 1
        elif s[left] != s[right]:
            return False
        elif s[left] == s[right]:
            right -= 1
            left += 1

    return True

'''  time Complexity: O(n)        space Complexity: O(1)  '''

''' Problem # 3: Remove Duplicates from Sorted Array: You are given a sorted integer array nums. 
                 Remove duplicates in-place such that each unique element appears only once. Return 
                 the number of unique elements.You must modify the array so that the first K elements contain the unique values.'''

# I failed at this, chatgpt solved This one, Because i misunderstood the problem.
def Duplicaters(nums, k):

    if not nums:
        return 0

    write = 1  # position to place next unique element

    for read in range(1, len(nums)):
        if nums[read] != nums[read - 1]:
            nums[write] = nums[read]
            write += 1

    return write

'''     Time Complexity = O(n)   Space Complexity = O(1)        ''' 

''' Problem # 4: Move Zeroes: Given an integer array nums, move all 0s to the end while maintaining the relative order of non-zero elements.
                 You must do it in-place without making a copy of the array.'''

def MoveZero(nums):

    right = 0
    Z = len(nums)
#    Zcount = 0 
    for left in range(len(nums)):
        if nums[left] != 0:
            nums[right] = nums[left]
            right += 1
        # else:
        #     Zcount += 1

    for el in range(right, Z):     # Chatpt asked me to used Right variable, my actual method was down below.
        nums[el] = 0

#    for el in range(Zcount):
#        nums[-el] = 0

    return nums                          

# Time complexity: O(n)    Space Complexity: 0(1)

'''Problem # 5: Squares of a Sorted Array: Given a sorted integer array nums (can contain negative numbers),
                return an array of the squares of each number sorted in non-decreasing order.'''

def SortMS(nums):

    Newnums = [0] * len(nums)
    
    for el in range(len(nums)):
        nums[el] = nums[el]**2

    point = -1
    left = 0
    right = len(nums) - 1

    while left <= right:
        if nums[left] < nums[right]:
            Newnums[point] = nums[right]
            right -= 1
            point -= 1
        else:
            Newnums[point] = nums[left]
            left += 1
            point -= 1
  
    return Newnums
''' Time Complexity:  O(n)     Space Complexity:  O(n)'''

nn = [-4,-1,2,3,10]
print(SortMS(nn))

def sortedMS_byGPT(nums):

    n = len(nums)
    res = [0] * n   # we need a pre-sized result array, that can be replaced by Actual squared items.

    left = 0
    right = n - 1
    pos = n - 1

    while left <= right:  # Here '<=' instead of just < make sure that the middle element also gets Processed. Read Pdf for more.
        if abs(nums[left]) > abs(nums[right]):
            res[pos] = nums[left] ** 2
            left += 1
        else:
            res[pos] = nums[right] ** 2
            right -= 1

        pos -= 1

    return res



    
    
        



    


            
               
               


        