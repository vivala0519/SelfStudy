from Algorithm_study.sort.sorts import bubblesort, selectionsort, insertionsort, insertionsort_2

assert bubblesort([4, 6, 2, 9, 1]) == [1, 2, 4, 6, 9]
assert bubblesort([3, 2, 1, 5, 3, 2, 3]) == [1, 2, 2, 3, 3, 3, 5]
assert selectionsort([4, 6, 2, 9, 1]) == [1, 2, 4, 6, 9]
assert selectionsort([3, 2, 1, 5, 3, 2, 3]) == [1, 2, 2, 3, 3, 3, 5]
assert insertionsort([4, 6, 2, 9, 1]) == [1, 2, 4, 6, 9]
assert insertionsort([3, 2, 1, 5, 3, 2, 3]) == [1, 2, 2, 3, 3, 3, 5]

assert insertionsort_2([4, 6, 2, 9, 1]) == [1, 2, 4, 6, 9]
assert insertionsort_2([3, 2, 1, 5, 3, 2, 3]) == [1, 2, 2, 3, 3, 3, 5]