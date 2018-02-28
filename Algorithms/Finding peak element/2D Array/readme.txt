Peak Finding

Objective: give any one peak element in a two dimensional array.

Peak value means that any value in the array is greater than that of the neighboring elements. In one dimensional array, we compare the element with it's left and right neighbor. In two dimensional array, we compare the element with top, down, left and right neighbors.

eg: [[1, 2, 4, 3, 5],
     [4, 5, 6, 1, 2],
     [8, 9, 2, 3, 5]]
In the above example, there are four peak elements. 6(6 > 4, 6 > 5, 6 > 1, 6 > 2), 9, 5(first row) and 5 (third row)(5 > 2, 5 > 3).

Hence for the end elements, two comparison is sufficient.

Now comes the question, Which peak element to choose?
Based on the Objective of the algorithm, we display out the first peak element we find.

Another questions is might arise: what if there is no peak element?
It turns out that there always exists atleast one peak element in the array, that is the maximum element in the array.

Approaches:

1. Linear Search
This is a simple straightforward method to find the peak value.

We go element by element in the array and compare the element with their neighbors and print out the peak element.

Complexity: O(n * m), saying n is number of rows and m is number of columns. At the worst case, it traverses through all the elements in the array.

2. Binary Search
This is the most optimal solution for solving this problem.

Step 1: we find the maxinum element at row n / 2. The max element means that it's greater than it's top and bottom neighbors.

Step 2: We check if the element of the array is a peak element by comparing it with it's left/right neighbors. if it is a peak element, we return it.

Step 3: If the middle element is not a peak element, then we split the number of rows(n) based on greater left/right neighbor. Hence eventually, the peak element is found.

Complexity: O(n * log(n)). O(n) is formed due to finding of index of max elementand O(log(n)) is formed due to spliting of array.

This is a lot faster compared to linear search when input array is too large.

