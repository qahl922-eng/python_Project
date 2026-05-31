'''Problem # 1: 3Sum Closest: Given an integer array nums and an integer target, return the sum of
                              the 3 integers that is closest to target, You may assume that each input has exactly one solution.'''

def Sum3Closest(nums, target):

    nums.sort()
    res = 0
    Summ = float('inf')            # its the largest possible int value, 'inf' means infinity. Read pdf for more.  
    for i, num in enumerate(nums):
        if i > 0 and num == nums[i-1]:
            continue
        l = i + 1
        r = len(nums) - 1
        while l < r:
            sumi = num + nums[l] + nums[r]
            checksum = target - sumi
            if abs(checksum) < Summ:    
                    Summ = abs(checksum)
                    res = sumi
            if sumi < target:
                l +=  1
            else:
                r -= 1
            

    return res
''' Time Complexity:  O(n2)         Space Complexity:  O(1) '''


'''Problem # 2: 4sum: Given an array nums and an integer target, return all unique quadruplets whose sum == target, a+b+c+d=target
                      such that: all 4 elements come from different indices, no duplicate quadruplets are allowed
 I solved it myself, but you can say that its 95% similar to 3sum, so...  its just okay. Don't get too excited '''


def Sum4(nums, target):

    res = [] 
    nums.sort()
     
    for i, num in enumerate(nums):
        if i > 0 and num == nums[i - 1]:
            continue

        for i2 in range(i + 1, len(nums)):
            if i2 > i + 1 and nums[i2] == nums[i2 - 1]:
                continue
            l = i2 + 1
            r  = len(nums) - 1

            while l < r:
                SUM = num + nums[i2] + nums[l] + nums[r]
                if SUM < target:
                    l += 1
                elif SUM > target:
                    r -= 1
                else:
                    res.append([num, nums[i2], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                    while nums[r] == nums[r + 1] and l < r:
                        r -= 1
    return res

'''    Time Complexity: O(n³)          Space Complexity: O(1)    '''

'''Problem # 3: Trapping Rain Water: You are given an array height where each value represents the height of a vertical bar
                After raining, water gets trapped between taller bars. Your have to calculate how much total water is trapped. '''
# Again, same problem # 3: I failed. This is a Chatgpt's solution

def rainwater(height):

    left = 0
    right = len(height) - 1

    leftMax = 0
    rightMax = 0

    water = 0

    while left < right:

        if height[left] < height[right]:
            # process left side
            if height[left] >= leftMax:
                leftMax = height[left]
            else:
                water += leftMax - height[left]
            left += 1

        else:
            # process right side
            if height[right] >= rightMax:
                rightMax = height[right]
            else:
                water += rightMax - height[right]
            right -= 1

    return water
        
'''Problem # 4: Longest Substring Without Repeating Characters: Given a string s, find the 'length' of the longest substring 
                that contains no repeating characters.'''
# Again, I failed. This is a Chatgpt's solution but its okay b/c this problem is way too unrelated to 3 sum.

def NonRepeat(s):

    seen = set()

    left = 0
    maxlength = 0

    for right in range(len(s)):

        while s[right] in seen:

            seen.remove(s[left])
            left += 1
        
        set.add(s[right])
        maxlength = max (maxlength, right - left + 1)    # read Case 3.4 inside Extra things in pdf to know how "right - left + 1" works. 
    
    return maxlength

'''  Timme Complexity: O(n)      Space Complexity: O(n)'''

'''Problem # 5: 3Sum Smaller: Given an integer array nums and an integer 'target', return the number of triplets such that:  a+b+c < target'''
# Again, I failed. This is a Chatgpt's solution but its okay.


def sum3Smaller(nums, target):

    nums.sort()
    T = 0
    for i, num in enumerate(nums):
#       if i > 0 and num == nums[i - 1]:                            Don't need duplicate skipping.
#           continue
        l = i + 1
        r = len(nums) - 1
        while l < r:
            sum1 = num + nums[l] + nums[r]
            if sum1 < target:                                     # Read About this Algoritms in Word Document, Case 3.5
                T += r - l
                l += 1
#               while nums[l] == nums[l + 1] and l < r:             since this problem don't want unique triplets only, so we can skip
#                   r -= 1                                          the duplicate skipping.           
            else:
                r -= 1
    return 'total unique triplets are:', T 


'''   Time Complexity: O(n2)          Space Complexity: O(1)   '''


'''Problem # 6: 3Sum Multi: Given an integer array nums and an integer 'target', return the number of triplets such that:  a+b+c <= target'''

def Multi3sum(nums, target):

    nums.sort()
    T = 0
    for i, num in enumerate(nums):
#       if i > 0 and num == nums[i - 1]:                            Don't need duplicate skipping.
#           continue
        l = i + 1
        r = len(nums) - 1
        while l < r:
            sum1 = num + nums[l] + nums[r]
            if sum1 <= target:                                     
                T += r - l
                l += 1
#               while nums[l] == nums[l + 1] and l < r:             since this problem don't want unique triplets only, so we can skip
#                   r -= 1                                          the duplicate skipping.           
            else:
                r -= 1
    return 'total unique triplets are:', T

'''   Time Complexity: O(n2)          Space Complexity: O(1)   '''
