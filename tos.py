#03 two odd split.py
#xor of two odd occouring numbers plitting by the rightmost set bit

input("xor all - pairs cancelll, two odd-occouring ones remain. press etner")
print(" [1,4,3,3] XOR of all:", 1 ^ 4 ^ 3 ^ 3, "  binary:", bin(1 ^ 4 ^ 3 ^ 3)[2:])
print(" split bit 1 --> group A (bit 0 ON): 1 group B (bit 0 OFF):  4")

n = int(input("enter a number(try 6 or 9):"))
guess= input("is the bit 0 of " + str(n) + " ON or OFF? (ON=1, OFF=0): ")
input("check the split bit. press enter")

if n & 1:
    print(" ", n, "binary:", bin(n)[2:], "bit 0 is ON", " ur guess:", guess)

else: 
    print(" ", n, "binary:", bin(n)[2:], "bit 0 is OFF", " ur guess:", guess)



