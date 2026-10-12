#! xor identity cancle
#xor iodentiy and equality and xor cancellation

input("xor with 0 keeps the number. press enter to continue")
print("   5 ^ 0 =", 5 ^ 0)
print("   0 ^ 5 =", 0 ^ 5)

input("xor with itself gives 0, press any key to conitinue")
print("   5 ^ 5 =", 5 ^ 5)
print("   0 ^ 0 =", 0 ^ 0)
n = int(input("enter a number, try 6 or 10: "))
guess= input("what is 3 ^" + str(n) + " ? ")
input("XOR cancels = 3 appears twice so it dissapears. press any key to continue")
print(" 3^", n,"^ 3=", 3 ^ n ^ 3, " ur guess:", guess)
