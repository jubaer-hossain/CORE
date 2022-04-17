def countBits(num):
    numberOfBits = 0
    while num:
        numberOfBits += num & 1
        print(num & 1) # 0, 0 , 1, 1
        num >>= 1 # num = num >> 1. Starts from the rightmost and sifts one bit at a time. So each iteration the number becomes: 1100 >> 110 >> 11 >> 1 >> 0(finally 0 and breaks the loop)
    print(num)
    return numberOfBits

print(countBits(12))

# Bitwise And
print(6 & 7) # 110 & 111 = 110
print (6 & 8) # 0110 & 1000 = 0000

# Bitwise Or
print(6 | 7) # 110 | 111 = 111 
print(6 | 8) # 0110 | 1000 = 1110(14)

# Bitwise XOR
print(6 ^ 7) # 110 ^ 111 = 001. a or b but not both
print(6 ^ 8) # 0110 ^ 1000 = 1110.
print(bin(8)) # 0b1000

# Bitwise left shift
print(8 << 2) # Shifts all bits of towards left by 2 digits. So it adds two extra digit at the right. 1000 becomes 1000,00

# Bitwise right shift
print(8 >> 2) # Shifts all bits of 8 towards right. So it adds two leading zeros at the back but leading zeros doesn't carry any value. 1000 become 0010. Basically removes
print(8 >> 4) # 0
print(8 >> 8) # 0 Cause 8 leading zeros is still zero

# Bitwise Not
"""
All binary has a sign bit. 0 -> Positive int. 1 -> Negative
13 -> 0, 1101
~13 -> 1, 0010 -> 2
But ~13 is actually -14

1s complement -> Flipping the bits
2s complement -> We add 1 to 1s complement

A negative number is stored as 2s complement in the machine

So -2 will be stored as 2s complement of it's binary representation. 
So 1s complement of 1,0010 is 1,1101
And 2s complement of 1,0010 is 1,1111 -> -14
-----

For quick calculation:
Add 1 with the binary representation of that number. 13 -> 1101 + 1 = 14 and add a negative sign to it
-----

Negative number's NOT. 
-13 is stored in binary as -13's 2s complement. Which is 12. 1101 0011 and ~0,0011 = 1,1100

Fast calculation:
Add 1 to the negative number and remove the sign.

CORE CONCEPT:
Basically, whenever we have a negative number, we need to convert it into it's 2s complement because machines store negative numbers in it's 2s complement. Then do the NOT operation. 
"""

print(~13) # -14
print(~(-13)) # 12
