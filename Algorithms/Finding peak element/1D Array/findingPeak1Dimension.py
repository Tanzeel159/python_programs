def getPeakValueInArray(array):
    n = len(array)
    if (n == 0):
        #array has no elements
        return 0
    elif (n < 3):
        #array has only one or two elements.
        return max(array)

    #array has 3 or more elements
    mid = int(n / 2)
    midValue = array[mid]
    paramArray = array

    if (midValue >= array[mid + 1] and midValue >= array[mid - 1]):
        return midValue
    elif (array[mid - 1] > array[mid + 1]):
        paramArray = array[0 : mid]
    else:
        paramArray = array[mid + 1 :]
    return getPeakValueInArray(paramArray)

if __name__ == "__main__":
    print(getPeakValueInArray([4, 5, 6, 3, 4, 5]))
    print(getPeakValueInArray([1, 2, 4, 3, 5]))
    print(getPeakValueInArray([1, 2, 3, 4, 5]))
