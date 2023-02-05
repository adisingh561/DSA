arr = []
for i in range(258*258):
    arr.append(i)

def get_range(arr,target):
    s=0
    e=2
    while (arr[e]<target):
        s=e+1
        e=e*e
    return(s,e)

print(get_range(arr,257))
