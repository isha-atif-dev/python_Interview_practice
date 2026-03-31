# Given a list of numbers, find the contiguous subarray that has the largest sum and return that sum.
# Example:
# [-2, 1, -3, 4, -1, 2, 1, -5, 4] → 6
# (subarray [4, -1, 2, 1] has the largest sum = 6)
# Example:
# [1] → 1
# [5, 4, -1, 7, 8] → 23

# brute force 

# def max_subarray(nums):
#     best = nums[0] #5
#     for i in range(len(nums)): #1
#         current = 0
#         for j in range(i,len(nums)):  #5 + 4 -1 + 7 
#             current += nums[j]
#             if current > best:
#                 best = current



    
    
# print(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))

# Kadane's algorithm
def max_array(nums):
    current = nums[0]
    best = nums[0]

    for num in nums[1:]:  
        current = max(num,current + num)
        best = max(best, current)

    return best

# print(max_array([5, 4, -1, 7, 8]))




