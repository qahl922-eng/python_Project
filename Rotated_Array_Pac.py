'''Main Problem: Search in Rotated Sorted Array:You are given an integer array nums sorted in ascending order, but the
                 array may have been rotated at some pivot unknown to you. Rotation means some front portion of the sorted
                 array was moved to the end.Your task is to find the index of a given target value in the array. If the target
                 exists, return its index; otherwise return -1. You must solve it as efficiently as possible.'''

# Although this problem is similar chatgpt's solution of the problem, I wrote the Double Condition logic myself.
def Rotated(nums, Target):
    l = 0
    r = len(nums) - 1

    while l <= r:

        mid = (l + r) // 2  # just one Bug, You have to put l + r inside ( ) because of higher precedence of '//'

        if Target == nums[mid]:
            return mid
        
        if nums[l] <= nums[mid]:
            if Target < nums[mid] and Target >= nums[l]:
                r = mid - 1
            else:
                l = mid + 1

        else:
            if Target > nums[mid] and Target <= nums[r]:
                l = mid + 1
            else:
                r = mid - 1
    return -1

'''Practice Problem # 01 — Find Minimum in Rotated Sorted Array: You are given a sorted array that has been rotated between 
                           1 and n times. Find the minimum element in the array. You must do it in O(log n).
                           Read pdf file to understnd the problem'''
# Although after many debuggings from GPT, this is my own solution

def rotatedsmall(nums):
    l = 0
    r = len(nums) - 1

    while l < r:

        mid = (l + r) // 2
        
        if nums[mid] > nums[r]:
            l = mid + 1

        else:
            r = mid
    return nums[l] 

''' Time Complexity: O(log n)      Space Complexity: O(1) '''

'''Practice Problem # 02 — Search in Rotated Sorted Array II: You are given a rotated sorted array nums that may contain duplicates,
                           and an integer target. Return True if target exists in the array, otherwise return False.'''
# Although with the help of one hint from chatGPT, But overall this is my solution
def roatatedII(nums, target):
    l = 0
    r = len(nums) - 1

    while l <= r:

        mid = (l + r) // 2

        if nums[mid] == target:
            return True
        if nums[l] == nums[mid] == nums[r]:  # This was a ChatGPT's Hint.
            l += 1
            r -= 1
            continue
        if nums[l] <= nums[mid]:
            if target < nums[mid] and nums[l] <= target:
                r = mid - 1
            else:
                l = mid + 1
        else:       
            if target > nums[mid] and nums[r] >= target:
                l = mid + 1
            else:
                r = mid - 1
    return False

''' Time Complexity: Average O(log n),      Worst O(n) (due to duplicates)            Space Complexity: O(1)''' 
# read Pdf for understanding multiple time complexity

'''Practice Problem # 03: Rotation Count: You are given a sorted array that has been rotated some number of times. 
                          Return how many times the array was rotated. Think of rotation as taking element from the 
                          end of the array and putting them at the front. Every time you rotate once, the smallest 
                          element moves one index forward'''

def RotationCount(nums):

    l = 0
    r = len(nums) - 1
    count = 0

    while l < r:

        mid = (l + r) // 2
        
        if nums[mid] > nums[r]:
            l = mid + 1
            count += 1
        else:
            r = mid

    return l

AA = [5,6,7,1,2,3,4]
print(RotationCount(AA))




