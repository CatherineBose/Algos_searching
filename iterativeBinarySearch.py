def iterativeBinarySearch (arr, start, end ,x):
    while start <= end :
        
        #calculate mid 
        mid = start + (end - start)//2
        print ("middle is now:",mid)
        print ("value at mid is:", arr[mid])
        
        # check if x is present than mid
        if arr[mid] == x:
            return mid
            
        
        # check if x is greater than mid
        # If x is greater, ignore left half
        elif  x > arr [mid]:
            print("I am in first elif")
            start = mid + 1
            print ("Current start index:", start)
            print ("value at start:", arr[start])
        
        #check if x is smaller than mid
        else:
            print("I am in last if")
            end = mid -1
            
    return -1

# Driver Code
arr = [2, 3, 4, 10, 40]
x = 10
n = len(arr) - 1

# Function call
result = iterativeBinarySearch(arr, 0, n, x)
if(result == -1):
    print("Element is not present in array")
else:
    print("Element is present at index", result)