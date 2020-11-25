
def binarySearch(array, num):
    
    mid = len(array)//2
    
    if len(array) == 1:
        if num == array[mid]:
            return True
        else:
            return False

    if array[mid] == num:
        return True
    elif num < array[mid]:
        return binarySearch(array[:mid], num)
    else:
        return binarySearch(array[mid:], num)

    
a = [1,4,8,20,24,33,61,109]
b = [1,4,8,20,24,33,61,109,201]



m = [[]]
def matrixSearch(matrix,target):
    m = matrix
    for i in range(0,len(m)):
        if binarySearch(m[i], target):
            return True
            break
    return False
