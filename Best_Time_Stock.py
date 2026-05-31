# i did on my own, just a theoratical explanation on YouTube from Neetcode.io with just a few bugs shown in code.
'''ChatGPt: 'Yes, your original solution will still give the correct answer in many cases, but it is logically weaker and less optimal' '''

def stocker(stocks):

    profit = 0

    left = 0
    right = left + 1

    while right < len(stocks):

        if stocks[left] < stocks[right]:
            profit = max(stocks[right] - stocks[left], profit)
#           right += 1       All these commented lines are part my original code which was a mistake.
        else: 
#           left += 1
            left = right   # Read 'Best time to Buy and sell stocks' Original solution.
#           right += 1

        right += 1         # we have to update 'right' with + 1 in every loop.
    
    return profit

'''Problem # X_X: Maximum Subarray: You are given an integer array nums. Your task is to find the contiguous 
                subarray (continuous part of the array meaning the elements must stay in their original 
                continuous order, so no sorting ) that has the largest possible sum and return that sum.'''

# By the way, it's a separate probelm itself on leetcode so i will not count it, i solved it  using chatGPT's Guaidance.

def maxsubarray(nums):

    Maxsum = nums[0]
    current = 0

    for el in range(len(nums)):

        current = max(nums[el], current + nums[el])

        Maxsum = max(Maxsum, current)

    return Maxsum

'''   Time: O(n)           Space: O(1)   '''

'''Problem # 1: Best Time to Buy and Sell Stock II: You are given a list of stock prices where each price represents the 
                stock value on a particular day. This time, unlike the previous problem, you are allowed to buy and sell
                the stock multiple times and you are allowed to sell and then buy again on the same day. However, you can
                only hold one stock at a time, meaning you must sell before buying again. Your task is to find the maximum
                total profit you can make.'''

def BeststockII(prices):

    left = 0 
    right = 1

    Bestsum = 0

    while right < len(prices):

        if prices[right] > prices[left]:

            Bestsum += prices[right] - prices[left]
            left = right
        
        else:
            left = right

        right += 1

    return Bestsum

'''   Time: O(n)           Space: O(1)   '''

'''Problem # 2: '''



























'''
currentsum = prices[right] - prices[left]
if right != len(prices) - 1:                          # This Block of code was my old solution for problem # 1, which was not optimal, 
    if prices[right] > prices[right + 1]:              But in this solution you can either buy or sell at a given day, not like the above 
        Bestsum += currentsum                          in which you can both buy and sell at a particular day.
        left = right
    elif right == len(prices) - 1:
        Bestsum = prices[right] - prices[left]'''

'''Problem # 1's : Chatgpt's solution: our mistake was that we 1st wrote the solution for the problem using 2 pointers in which we can either
                   buy or sell at given day and than converted that same 2_pointers based solution to that solution above, but chatGPT used 
                   simple for loop and updated the the profit if there was any.'''
def BeststockII(prices):

    profit = 0

    for i in range(1, len(prices)):

        if prices[i] > prices[i - 1]:

            profit += prices[i] - prices[i - 1]

    return profit



        