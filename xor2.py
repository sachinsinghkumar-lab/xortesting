#odd occouring.pyo
#one odd occouring number

input("XOR all numbers=paircs cancel the odd one stayus. press enter")
print("list : [2,3,4,3,2]")
print("odd occouring:", 2 ^ 3 ^ 4 ^ 3 ^ 2)

n = int(input("enter a number(try 7 or 11):"))
nums = [3, n, 5, 3, 5]
guess = input("which number in" + str(nums) + "appears once?")
result  = 0 
for x in nums:
    result ^= x
input("XOR all numbers=paircs cancel the odd one stayus. press enter")
print("lists:", nums, " odd occoouring:", result, " ur guess:", guess)
