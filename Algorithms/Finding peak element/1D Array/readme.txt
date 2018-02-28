Peak Finding

Objective: give any one peak element in the array.

Peak value means that any value in the array is greater than that of it's left/right neighbors.

eg 1: [1, 2, 3, 4, 2]
In the above example, 4 is the peak element as 4 > 2 and 4 > 3.

eg 2: [1, 2, 4, 3, 5]
In the above example, there are two peak elements. 4 and 5 (as 5 > 3). Hence for
the end elements, one comparison is sufficient.

Now comes the question, Which peak element to choose?
Based on the Objective of the algorithm, we display out the first peak element we find.

Another questions is might arise: what if there is no peak element?
It turns out that there always exists atleast one peak element in the array, that is the maximum element in the array.

Approaches:

1. Linear Search
This is a simple straightforward method to find the peak value.

We go element by element in the array and compare the element with their neighbors and print out the peak element.

Linear search can be used to find the highest peak element.(which is basically finding the max value in the array)

Complexity: O(n). At the worst case, it traverses through the entire array.

2. Binary Search
This is the most optimal solution for solving this problem.
We check if the middle element of the array is a peak element. if it is a peak element, we return it.
If the middle element is not a peak element, then we split the array based on greater neighbor. Hence eventually, the peak element is found.

Complexity: O(log(n)). This is a lot faster compared to linear search when input array is too large.

