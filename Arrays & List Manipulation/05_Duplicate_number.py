# Question 9 — Find the Duplicate Number

# Given a list of n+1 integers where every integer is between 1 and n, there is exactly one duplicate number. Find and return it.
# Example:
# [1, 3, 4, 2, 2] → 2
# [3, 1, 3, 4, 2] → 3

def is_duplicate(nums):
    freq = {}
    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    for item in freq:
        if freq[item] > 1:
            return item 
        


print(is_duplicate([1, 3, 4, 2, 2]))
# space O(n)

# optimized version

def find_duplicate(nums):
    seen = set()

    for num in nums:
        if num in seen:
            return num
        seen.add(num)

print(is_duplicate([1, 3, 4, 2, 2]))

# now space O(1)
