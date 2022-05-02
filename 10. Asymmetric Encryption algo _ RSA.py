import math
message = int(input("Enter the message to be encrypted: "))
p = 11
q = 7
e = 3
n = p * q
def encrypt(me):
    en = math.pow(me, e)
    c = en % n
    print("Encrypted Message = ", c)
    return c
print("Original Message = ", message)
c = encrypt(message)
#message = 7412