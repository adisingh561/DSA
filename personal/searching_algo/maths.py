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
    # right shift and get that digit by and 1
    #can also use while loop keep on right shift till you get 0 
    #using above logic can also find number of digit in base b 
    for i in range(1,n+1):
        result+=(((n>>(i-1)&1)*pow(5,i)))

    return result
# print(n_magic(6))

#Number of digit in base b of a number 
import math
def number_of_dig(num,base):
    return (int(math.log(num)/math.log(base))+1)
# print(number_of_dig(10,2))

#sum of nth row of pascals triangle -> 2 power (n-1)
def pascal_sum(row):
    return (1<<(row-1))
# print(pascal_sum(6))

#Is a number a power of 2 or not 
def power_of_2(num):
    if num == 0 :
        return False
    return bool(((num) & (num-1))==0)

# print(power_of_2(512))