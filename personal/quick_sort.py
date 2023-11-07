def QuickSort(arr,low,high):
    if low >= high :
        return
    s=low
    e=high
    m = int((e-s)/2)
    pivot = arr[m]
    while s<=e:
        while arr[s]<pivot:
            s+=1
        while arr[e]> pivot:
            e-=1
        if s<= e:
            temp = arr[s]
            arr[s]=arr[e]
            arr[e]=temp
            s+=1
            e-=1
    #Now pivot at right place so run on part
    QuickSort(arr,low,e)
    QuickSort(arr,s,high)

print(QuickSort([3,4,5,1,2],0,5))