def MergeSort(arr):
    if len(arr) == 1 :
        return arr
    mid = int(len(arr)/2)
    arr1 = MergeSort(arr[0:mid])
    arr2 = MergeSort(arr[mid:len(arr)])
    #Merge array
    arr3 = []
    i=0
    j=0
    while (i<len(arr1) and j<len(arr2)):
        if arr1[i]<arr2[j]:
            arr3.append(arr1[i])
            i+=1
        else:
            arr3.append(arr2[j])
            j+=1
    #Now if one of the array not complete
    while (i<len(arr1)):
        arr3.append(arr1[i])
        i+=1
    while (j<len(arr2)):
        arr3.append(arr2[j])
        j+=1
    return arr3

def merge(arr1,arr2):
    arr3 = []
    i=0
    j=0
    while (i<len(arr1) and j<len(arr2)):
        if arr1[i]<arr2[j]:
            arr3.append(arr1[i])
            i+=1
        else:
            arr3.append(arr2[j])
            j+=1
    #Now if one of the array not complete
    while (i<len(arr1)):
        arr3.append(arr1[i])
        i+=1
    while (j<len(arr2)):
        arr3.append(arr2[j])
        j+=1
    return arr3
def MergeSort1(arr):
    if len(arr)==1:
        return arr
    mid = int((len(arr))/2)
    left = MergeSort(arr[0:mid])
    right = MergeSort(arr[mid:len(arr)])
    return merge(left,right)

print(MergeSort(arr=[38, 27, 43, 3, 9, 82, ]))
