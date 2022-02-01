from Algorithm_study.sort.sorts import bubblesort, selectionsort, insertionsort, insertionsort_2, quicksort, merge_sort

assert bubblesort([4, 6, 2, 9, 1]) == [1, 2, 4, 6, 9]
assert bubblesort([3, 2, 1, 5, 3, 2, 3]) == [1, 2, 2, 3, 3, 3, 5]

assert selectionsort([4, 6, 2, 9, 1]) == [1, 2, 4, 6, 9]
assert selectionsort([3, 2, 1, 5, 3, 2, 3]) == [1, 2, 2, 3, 3, 3, 5]

assert insertionsort([4, 6, 2, 9, 1]) == [1, 2, 4, 6, 9]
assert insertionsort([3, 2, 1, 5, 3, 2, 3]) == [1, 2, 2, 3, 3, 3, 5]

assert insertionsort_2([4, 6, 2, 9, 1]) == [1, 2, 4, 6, 9]
assert insertionsort_2([3, 2, 1, 5, 3, 2, 3]) == [1, 2, 2, 3, 3, 3, 5]

assert quicksort([4, 6, 2, 9, 1], 0, 1) == [4, 6, 2, 9, 1]
assert quicksort([4, 6, 2, 9, 1], 0, 2) == [2, 4, 6, 9, 1]
assert quicksort([4, 6, 2, 9, 1], 0, 3) == [2, 4, 6, 9, 1]
assert quicksort([4, 6, 2, 9, 1], 0, 4) == [1, 2, 4, 6, 9]
assert quicksort([3, 2, 1, 5, 3, 2, 3], 0, 1) == [2, 3, 1, 5, 3, 2, 3]
assert quicksort([3, 2, 1, 5, 3, 2, 3], 0, 2) == [1, 2, 3, 5, 3, 2, 3]
assert quicksort([3, 2, 1, 5, 3, 2, 3], 0, 3) == [1, 2, 3, 5, 3, 2, 3]
assert quicksort([3, 2, 1, 5, 3, 2, 3], 0, 4) == [1, 2, 3, 3, 5, 2, 3]
assert quicksort([3, 2, 1, 5, 3, 2, 3], 0, 5) == [1, 2, 2, 3, 3, 5, 3]
assert quicksort([3, 2, 1, 5, 3, 2, 3], 0, 6) == [1, 2, 2, 3, 3, 3, 5]

assert merge_sort([4, 6, 2, 9, 1]) == [1, 2, 4, 6, 9]
assert merge_sort([3, 2, 1, 5, 3, 2, 3]) == [1, 2, 2, 3, 3, 3, 5]