arr=[64,36,74,12,85,7]
for i in range(len(arr)):
    min_index=i
    for j in range(i+1,len(arr)):
        if(arr[j]<arr[min_index]):
            min_index=j
    arr[i],arr[min_index]=arr[min_index],arr[i]
print("sorted:")
print(arr)            
