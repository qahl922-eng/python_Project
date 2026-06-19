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

def rotated3(nums):
    l = 0
    r = len(nums) - 1

    while l <= r:

        mid = (l + r) // 2
        
        if nums[l] <= nums[mid]:
            if nums[mid] > nums[r] or nums[l] > nums[r]:

        
        else:



