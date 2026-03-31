# # The setup
# # You have a staircase. You start at the bottom. You want to reach the top.
# # Every single step you take, you can either:

# # jump 1 step
# # OR
# # jump 2 steps

# # The question is — how many different ways exist to reach the top?

# # n = top  number of stairs

# So what is the input and output?
# Input  → one number n  (how many stairs)
# Output → one number    (how many different paths exist)

# climb_stairs(4) → 5
# climb_stairs(5) → 8
# climb_stairs(3) → 3

def climb_stairs(n):
    if n == 1:
        return 1
   
    step_one = 1
    step_two = 2

    for i in range(3, n+1):
      current = step_one + step_two
      step_one = step_two
      step_two = current

    return step_two

print(climb_stairs(5))