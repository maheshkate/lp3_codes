def isprime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in range(3,int(num ** 0.5) + 2,2):
        if num % n == 0:
            return False
    return True

g = int(input("Enter the first prime number"))
if(not isprime(g)):
    print(g,"is not a prime number")
else:
    p = int(input("Enter the second prime number"))
    if(not isprime(p)):
        print(p,"is not a prime number")
    else:
        a = int(input("Enter user1 secret key "))
        A = (g ** a)%p
        print("User1 will send ",g,p,A)
        b = int(input("Enter user2 secret key "))
        B = (g ** b)%p
        print("User2 will send ",g,p,B)
        K1 = (B ** a)%p
        K2 = (A ** b)%p
        if(K1 == K2):
            print("Symmetric key is",K1)
        else:
            print("Something went wrong")