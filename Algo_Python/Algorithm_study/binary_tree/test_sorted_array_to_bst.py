from Algorithm_study.binary_tree.prac import make_lst_by_bst, sorted_array_to_bst

def test_sorted_array_to_bst(lst):
    if not lst:
        return []
    root = sorted_array_to_bst(lst)
    return make_lst_by_bst(root, len(lst))


assert test_sorted_array_to_bst(lst=[-10, -3, 0, 5, 9]) == [0, -3, 9, -10, None, 5]
assert test_sorted_array_to_bst(lst=[-10, -7, -3, -1, 0, 1, 4, 5, 7, 9]) == [1, -3, 7, -7, 0, 5, 9, -10, None, -1, None]