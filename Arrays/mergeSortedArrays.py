def mergeSortedArrays(arr1, arr2):
    m, n = len(arr1), len(arr2)

    left, right = m - 1, 0

    while left>=0 and right<n:
        if arr1[left]>arr2[right]:
            arr1[left], arr2[right] = arr2[right], arr1[left]
            left-=1
            right+=1
        else:
            break
    
    arr1.sort()
    arr2.sort()

arr1 = [1, 4, 8, 10]
arr2 = [2, 3, 9]

mergeSortedArrays(arr1, arr2)

print("The merged arrays are:")
print("arr1[] = ", end="")
for i in range(len(arr1)):
    print(arr1[i], end=" ")
print("\narr2[] = ", end="")
for i in range(len(arr2)):
    print(arr2[i], end=" ")
print()