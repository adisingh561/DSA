
def swap(arr,pos1,pos2):
    temp = arr[pos1]
    arr[pos1] = arr[pos2]
    arr[pos2] = temp
    return arr

def cyclic_sort(arr:list):
    i=0
    while(i<len(arr)):
        index_correct = arr[i]
        if int(arr[i]) != arr[index_correct]:
            arr = swap(arr,i,index_correct)
        else :
            i+=1
    return arr
array = [2,1,0]

# def findMax(arr):
#     max = arr[0]
#     for i in range(len(arr)):
#         if arr[i]>
print(cyclic_sort(array))