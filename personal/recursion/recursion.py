#print a func that prints 1-> 5 using recursion
#SIMPLE
def printn(n):
    print(n)
    if n<10:
        return printn(n+1)
# printn(1)

#FIB NOS
def fib(N):
    if N == 0:
        return 0
    if N == 1 or N==2:
        return 1
    return fib(N-1)+fib(N-2)

# BinarySearch
def BS(arr,target,s,e):
    if s>e :
        return -1
    m = int(s+(e-s)/2)
    if arr[m] == target:
        return m
    if arr[m]< target:
        return BS(arr,target,m+1,e)
    return BS(arr,target,s,m-1)
arr = [1,2,3,4,5,6,7,9,15,22]
# print(BS(arr,11,0,len(arr)-1))