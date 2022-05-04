def merge(A,low, mid, high):
    k = i = low
    j = mid + 1
    temp = A.copy()
    # while there are elements in the left and right runs
    while i <= mid and j <= high:
        if A[i] <= A[j]:
            temp[k] = A[i]
            i = i + 1
        else:
            temp[k] = A[j]
            j = j + 1

        k = k + 1

    # copy remaining elements
    while i <= mid:
        temp[k] = A[i]
        k = k + 1
        i = i + 1

    ''' no need to copy the second half (since the remaining items
        are already in their correct position in the temporary array) '''

    # copy back to the original list to reflect sorted order
    for i in range(low, high + 1):
        A[i] = temp[i]

    return A


# Sort list A[low…high] using auxiliary list aux
def mergesort(A,low, high):
    # base case
    if high <= low:  # if run size <= 1
        return 0

    # find midpoint
    mid = int((low+high)/2)
    invCnt = 0

    # recursively split runs into two halves until run size <= 1,
    # then merges them and return up the call chain

    mergesort(A,low, mid)  # split/merge left half
    mergesort(A, mid + 1, high)  # split/merge right half
    merge(A,low, mid, high)  # merge the two half runs


# Driver code to test above
arr = list(map(int,input("Enter values:").split()))
n = len(arr)
print("Given array is")
for i in range(n):
    print("%d" % arr[i], end=" ")

mergesort(arr, 0, n - 1)
print("\n\nSorted array is")
for i in range(n):
    print("%d" % arr[i], end=" ")
