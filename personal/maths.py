#ODD/EVEN
def isodd(num):
    return (num & 1 == 1)
#print(isodd(12))

#FIND UNIQUE in a double repeating array
def isunique(arr):
    a=0
    for i in range(len(arr)):
        a^=(arr[i])
    return a
# print(isunique([1,2,4,4,3,2,1]))

#nth magic number -> number to binary the digits multiply by powers of 5
#eg 1st magic = 1*5^1 = 5 ; 2nd -> 2= (1,0) -> 1*5^2 + 0*5^1 = 25 ; 3rd = (1,1) = 30 and so on 
def n_magic(n):
    result = 0
    # if n ==1 :
    #     return result
    for i in range(1,n+1):
        result+=(((n>>(i-1)&1)*pow(5,i)))

    return result
# print(n_magic(6))

