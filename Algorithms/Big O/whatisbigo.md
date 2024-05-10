__Big-O Notation__
Analyze and describe the efficiency of algorithms runtime and usage of resources grow as input data increases.

i.e.: cooking pasta - How long it will take to boil water?
- consider size of pot, stove power, amount of water

Big-O answer questions like:
• How does the runtime of an algorithm change as the input data gets larger?
• How does an algorithm scale with increased input size?

Big-O - 'O(function)'

__Constant time__ - O(1) - when runtime does not depend on size of input data remaining constant.

i.e.: accessing an array by its index takes the same amount of time no matter how large the array is.
def access_element(arr, index):
    return arr[index] 


__Linear Time__ - O(n) - runtime grows linear (progressive) as input data increases

i.e.: searching for specific value in unsorted list
def linear_search(arr, target): //as arr grows the runtime increases
    for item in arr: 
        if item == target:
            return True
    return False

__Quadratic Time__ - O(n^2) - grows with the square of the input size, as data increases, runtime increases quadratically.

i.e.: Bubble Sort, a simple sorting algorithm.
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i -1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

__logarithmic Time__ - O(log n) - runtime grows logarithmically with the size of input data - very efficient

i.e.: Binary search in a sorted list.
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == targett:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
        return -1

    drastically reduces search time as the size of the sorted list arr grows.


A Quick Breakdown

Fastest:

O(1) - Constant Time: Lightning-fast! The algorithm's speed doesn't depend on how much data you have. It's like finding your favorite book on a perfectly organized bookshelf – it takes the same amount of time, whether you have 10 books or 1,000 books.
Pretty Fast:

O(log n) - Logarithmic Time: Still quite speedy! It grows slowly as you add more data. Think of it as finding a name in a phone book by repeatedly splitting it in half – it gets faster even if the phone book gets bigger.
Moderate:

O(n) - Linear Time: Respectable speed! If you have twice as much data, it takes about twice as long. It's like looking through a list of names one by one to find a match.
Slower:

O(n log n) - Linearithmic Time: It's faster than quadratic but slower than linear. Comparable to sorting a deck of cards quickly using smart techniques.
Slower Still:

O(n^2) - Quadratic Time: Getting slower as you add data. Like checking every combination of items on a list against each other – not great for large lists.
Quite Slow:

O(2^n) - Exponential Time: Now we're talking about slow! It grows rapidly as you add data. Imagine a puzzle where you have to try every possible combination – it's really slow even for small puzzles.
Incredibly Slow:

O(n!) - Factorial Time: The slowest of all! It's like solving a complex puzzle where the number of possible arrangements explodes as you add more pieces. Practically unusable for large problems.



Big O notation is crucial for several reasons:
__Algorithm Comparison__ - It allows us to objectively compare different algorithms and choose the most efficient one for a specific task.
__Performance Optimization__ -  Understanding Big O helps identify bottlenecks in code and optimize algorithms for better performance.
__Scalability__ -  Efficient algorithms are vital as applications and data sizes grow.
__Resource Management__ - In resource-constrained environments, like embedded systems, choosing efficient algorithms is essential.
__Coding Interviews__ -` Big O notation is often tested in technical interviews and coding challenges, demonstrating your ability to analyze and optimize algorithms.



Analyzing Code with Big O Notation

To analyze code using Big O notation, follow these steps:

Identify the Input Size: Determine what "n" represents in your code, often related to the size of the input data.
Identify Loops and Iterations: Look for loops in your code, as they often determine the primary factors affecting time complexity.
Count Operations Inside Loops: Count the number of operations inside each loop that depend on the input size "n."
Combine Complexity: If you have nested loops, multiply their complexities to determine the overall time complexity.
Choose the Dominant Term: In cases of combined complexity, focus on the term with the highest growth rate, as it will dominate the overall time complexity.
Simplify: Simplify the expression as much as possible by removing constant factors.