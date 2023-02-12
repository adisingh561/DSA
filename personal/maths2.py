import math
#PRIME NUMBER 
def is_prime(num):
    if num<=1:
        return False
    i=2
    while (i*i <= num):
        if num%i == 0:
            return False
        i+=1
    return True
# print(is_prime(61))

#All prime nos less than a number -> SieveOfEratosthenes
def SieveOfEratosthenes(n):
    prime = [True for i in range(n+1)]
    i=2
    while (i*i<=n):
        if prime[i] == True:
            for j in range(i*i,n+1,i):
                prime[j]=False
        i+=1
    for i in range(2,n+1):
        if prime[i]:
            print(i)
# print(SieveOfEratosthenes(40))

#Sq root of a number upto 3 decimal
def BinarySearchSQRT(num,decimal):
    s = 0
    e=int(num/2)
    root = 0.0
    while(s<=e):
        m = int(s+(e-s)/2)
        if (m*m == num):
            return m
        elif (m*m > num):
            e = m-1
        else :
            s=m+1
    root = float(e)

    incr = 0.1
    for i in range(decimal):
        while(root*root<=num):
            root+=incr
        root-=incr
        incr /= 10
    return root
    # print(40**0.5) -> Python inbuilt sqrt method
# print("%.5f"%BinarySearchSQRT(40,5))

#Sq root using Newton Raphson's
def NewtonRaphsoSQRT(num):
    x=float(num)
    root = float(1)
    while True:
        root = 0.5 *(x+(num/x))
        if abs(root-x)<0.5:
            break
        x= root
    return root
# print(NewtonRaphsoSQRT(40))

#GCD using Euclids theorm gcd(a,b) = gcd((b%a),a) until a = 0 -> Time_complexity = log(min(a,b))
def gcd(a,b):
    if a == 0:
        return b
    return gcd((b%a),a)
# print(gcd(19,4)) 

#lcm(a,b)=(a*b)/gcd(a,b)
def lcm(a,b):
    return int((a*b)/gcd(a,b))

# print(lcm(3,14))


