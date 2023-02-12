#Check if array sorted using recursion -> if don't want to modify arr then can use a pointer as an argument
def is_sorted(arr:list):
    if len(arr) == 2 :
        return (arr[0]<arr[1])
    elif len(arr)>2:
        arr.pop(0)
        return (arr[0]<arr[1] and is_sorted(arr))
    else:
        return True
# print(is_sorted(arr=[1,2,3,4,7,8,66]))

#Return an array list with indices of target in a given array -> without passing ans arraylist as arg
def is_instance(arr,target,i=0):
    l=[]
    if i == len(arr)  :
        return []
    if arr[i]==target :
        l.append(i)
        i+=1
    else :
        i+=1
    #Adding answers from below basically
    l= l.__add__(is_instance(arr,target,i))
    return l 
arr = [1,2,3,4,4,4,5]
print(is_instance(arr=arr,target=4,i=0))


    
