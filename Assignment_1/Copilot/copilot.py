#program to bubble sort in python

# Python program for implementation of Bubble Sort

def bubbleSort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):

        # Last i elements are already in place
        for j in range(0, n-i-1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]

def printArray(arr):
    for i in range(len(arr)):
        print("% d\t" % arr[i])
        
# Driver code to test above
arr = [64, 34, 25, 12, 22, 11, 90]
print("Unsorted array is:")
printArray(arr);
print("Bubble Sorted array is:")
bubbleSort(arr)
printArray(arr)

#Insertion Sort in Python
def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key
        
# Driver code to test above
arr = [12, 11, 13, 5, 6]
print("Unsorted array is:")
printArray(arr)
print("Inserion Sorted array is:")
insertionSort(arr)
printArray(arr)

#quick sort in python
def partition(arr,low,high):
    i = ( low-1 )         # index of smaller element
    pivot = arr[high]     # pivot

    for j in range(low , high):

        # If current element is smaller than or
        # equal to pivot
        if   arr[j] <= pivot:

            # increment index of smaller element
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]

    arr[i+1],arr[high] = arr[high],arr[i+1]
    return ( i+1 )

# Function to do Quick sort
def quickSort(arr,low,high):
    if low < high:

        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr,low,high)

        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)
        
# Driver code to test above
arr = [10, 7, 8, 9, 1, 5]
print("Unsorted array is:")
printArray(arr)
print("Quick Sorted array is:")
quickSort(arr,0,len(arr)-1) 
printArray(arr)   








