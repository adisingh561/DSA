#print 12345 then 54321 see the diff in pos of print statement
def fun(n):
    if n==0:
        return
    fun(n=n-1)
    print(n)
def fun_rev(n):
    if n==0:
        return
    print(n)
    fun_rev(n=n-1)
    
# fun(5)
# fun_rev(5)

#Factorial of a number
def factorial(n):
    if n == 0 :
        return 1
    if n==1:
        return 1
    return (n*factorial(n-1))
    # return ans
# print(factorial(5))

#Sum of digits 1342
def digit_sum (num):
    if num == 0:
        return 0
    return (num%10) + digit_sum(int(num/10))

#Multipication of digits
def digit_multi (num):
    #See how to check for number == 0
    #if one digit remaining retrun the digit
    if num%10 == num:
        return num
    return (num%10) * digit_multi(int(num/10))   
# print(digit_multi(1240))

#Reverse a number using recursion -> ********** / can use an extra variable outside as well /
# or can use helper function ie make a new function
import math
def rev(num):
    place = int(math.pow(10,int(math.log10(num))))
    if num%10 == num :
        return(num)
    return (num%10)*place + rev(int(num/10))     
# print(rev(112045))

#Palindrome -> can use rev function -> else array and 2 pointers
def palindrome(num):
    return num == rev(num)
# print(palindrome(1123211))

#Count number of zeros in a number using recursion -> can use a count in args as well
def zero_count(num):
    if num%10 == num :
        return 0
    else:
        if num%10 == 0:
            return 1+zero_count(int(num/10))
        return zero_count(int(num/10))
# print(zero_count(1100011))

#leetcode 1342 -> Number of steps to reduce a number to zero -> ********
def c(num,count=0):
    if num == 0 :
        return count
    if num%2 == 0:
        count+=1
        return c(num/2,count)
    else :
        count+=1
        return c(num-1,count)

print(c(8))