def selectionSort(arr,arrsize):
    for i in range(arrsize):
        k = i
        for j in range(i + 1,arrsize):
            if arr[j] < arr[k]:
                k = j
        (arr[i],arr[k])=(arr[k],arr[i])
arrsize=int(input("Enter the number of elements:"))
arr=[]
for i in range(arrsize):
    arr.append(int(input("Enter the elements:")))
print("The array before sorting is:",arr)
selectionSort(arr,arrsize)
print("The array after sorting is:",arr)
