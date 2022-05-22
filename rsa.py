import random

def gcd(a,b):
    while b != 0:
        a,b = b, a % b
    return a

def multiplicative_inverse(e,phi):
    for i in range(phi):
        if((e*i)%phi == 1):
            return i

def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in range(3,int(num ** 0.5) + 2,2):
        if num % n == 0:
            return False
    return True

def generate_keypair(p,q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError("Both numbers must be prime.")
    elif p == q:
        raise ValueError("p and q cannot be equal")

    n = p * q

    phi = (p - 1) * (q - 1)

    e = random.randrange(1,phi)
    
    g = gcd(e,phi)
    while g != 1:
        e = random.randrange(1,phi)
        g = gcd(e,phi)

    d = multiplicative_inverse(e,phi)
    print("D is ")
    return ((e,n),(d,n))

def encrypt(pk,plainText):
    key,n = pk
    cipher = [(ord(char) ** key) % n for char in plainText]

    return cipher

def decrypt(pk,cipherText):
    key,n = pk
    plain = [chr((char ** key) % n) for char in cipherText]

    return ''.join(plain)

if __name__ == '__main__':

    print("RSA Encrypter/Decrypter")
    
    p = int(input("Enter a prime number"))
    q = int(input("Enter another prime number other than previous one"))
    public, private = generate_keypair(p,q)

    print("Public Key",public," private Key",private)

    message = input("Enter a message to encrypt with private key: ")
    encrypted_msg = encrypt(private,message)

    print("Encrypted text")
    print(''.join(map(lambda x : str(x),encrypted_msg)))

    print("Decrypting message with public key")
    print("Message is")
    print(decrypt(public,encrypted_msg))