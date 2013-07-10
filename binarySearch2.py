#Alexander Starr
#22C:016:A01
#00567613

def binarySearch(L, k):
    left = 0 
    right = len(L)-1
    
    if left > right:
        return 0
    
    # iterate until there is a sublist that needs to be searched
    while left <= right:
        mid = (left + right) / 2  # index of the middle element
        # Comparisons and then adjusting the boundaries of
        # the sublist, if necessary
        if L[mid] == k:
            return mid # element is found at mid, so return this index
        elif L[mid] < k: # look for element in right half
            left = mid + 1
        elif L[mid] > k: # look for element in the left half
            right = mid - 1
            
    # element is not found in the list
    if L[mid] < k:
        return mid + 1
    else:
        return mid