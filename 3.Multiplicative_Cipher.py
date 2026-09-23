import math as omgmath # imporing math module
a = input("Enter a letter :").upper()#input of letter
key = int(input("Enter a key :"))#input of key
if len(a) != 1:
    print("Invalid Input")
    exit()
if omgmath.gcd(key, 26) != 1:
    print("invalid key")
    exit()
p = ord(a) - ord('A')#converts input letter to a number from 0-25
c = (p * key) % 26 #implements formula
cipher = chr(c + ord('A'))#convert number back to letter
key_inverse = pow(key, -1, 26) # finds the invers of key key^-1 mod 26
decrypt = (c * key_inverse) % 26 #decrypts the cypher text
decrypta = chr(decrypt + ord('A')) # decrypted turned back into a letter by chr function
print("plaintext:", a)
print("key:", key)
print("plaintext value:", p)
print("ciphertext:", cipher)
print("ciphertext value:", c)
print("key inverse:", key_inverse)
print("decrypted value:", decrypt)
print("decrypted text:", decrypta)
