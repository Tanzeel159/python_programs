def indexOfMaxValueInArray(array): #array:- [Int]
    maxValueIndex = 0
    n = len(array)
    for i in range(n):
        if array[maxValueIndex] < array[i]:
            maxValueIndex = i
    return maxValueIndex


def findingPeak2Dimension(array): #array:- [[Int]]
    #assuming array is not empty.
    n = len(array)
    mid = int(n / 2)
    indexOfMaxValue = indexOfMaxValueInArray(array[mid])
    maxMidValue = array[mid][indexOfMaxValue]
    if(n == 1):
        return maxMidValue
    elif(n == 2):
        itsLeftNeighbor = array[mid - 1][indexOfMaxValue]
        if(maxMidValue >= itsLeftNeighbor):
            return array[mid][indexOfMaxValue]
        else:
            return itsLeftNeighbor
    else:
        itsLeftNeighbor = array[mid - 1][indexOfMaxValue]
        itsRightNeighbor = array[mid + 1][indexOfMaxValue]

        if(maxMidValue >= itsLeftNeighbor and maxMidValue >= itsRightNeighbor):
            return maxMidValue
        elif(itsLeftNeighbor >= itsRightNeighbor):
            return findingPeak2Dimension(array[: mid])
        else:
            return findingPeak2Dimension(array[mid + 1:])



if __name__ == "__main__":
    print(findingPeak2Dimension([[1, 2, 3, 4, 5], [5, 8, 9, 4, 6], [3, 8, 5, 3, 2]]))
