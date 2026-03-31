# Question 10 — Single Number

# Every element in a list appears twice except for one. Find that single one.
# Example:
# [2, 2, 1] → 1
# [4, 1, 2, 1, 2] → 4
# [1] → 1

def is_single(nums):
    freq = {}
    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    for num in freq:
        if freq[num] == 1:
            return num
        
print(is_single([2, 2, 1]))

# if we want to optimzed it like doing Space O(1)

def single(nums):
    result = 0
    for num in nums:
        result ^= num
    return result

print(single([2, 2, 1]))


# using XOR means 

# if both 2 ^ 2 then 0 (2 same number gives 0)

# if 1 ^ 0 then 1 (this is how we get singular)

