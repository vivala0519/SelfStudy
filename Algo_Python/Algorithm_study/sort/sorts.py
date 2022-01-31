def bubblesort(lst):
    # 최댓값을 구하는 알고리즘을 len(lst) - 1 만큼 반복한다.
    iters = len(lst) - 1
    for iter in range(iters):
        # 이미 구한 최댓값은 범위에서 제외한다.
        wall = iters - iter
        for cur in range(wall):
            if lst[cur] > lst[cur + 1]:
                lst[cur], lst[cur + 1] = lst[cur + 1], lst[cur]
    return lst

def selectionsort(lst):
    iters = len(lst) - 1
    for iter in range(iters):
        minimum = iter
        for cur in range(iter + 1, len(lst)):
            if lst[cur] < lst[minimum]:
                minimum = cur
            
        if minimum != iter:
            lst[minimum], lst[iter] = lst[iter], lst[minimum]
    
    return lst

def insertionsort(lst):
    # 0번째 요소는 이미 정렬되어있으니, 1번째 ~ lst(len)-1 번째를 정렬하면 된다.
    for cur in range(1, len(lst)):
        # 비교지점이 cur-1 ~ 0(=cur-cur)까지 내려간다.
        for delta in range(1, cur + 1):
            cmp = cur - delta
            if lst[cmp] > lst[cmp + 1]:
                lst[cmp], lst[cmp + 1] = lst[cmp + 1], lst[cmp]
            else:
                break
    return lst

def insertionsort_2(lst):
    for idx in range(1, len(lst)):
        val = lst[idx]
        cmp = idx - 1

        while lst[cmp] > val and cmp >= 0:
            lst[cmp + 1] = lst[cmp]
            cmp -= 1

        lst[cmp + 1] = val
    
    return lst

def quicksort(lst, start, end):
    def partition(part, ps, pe):
        pivot = part[pe]
        i = ps - 1
        for j in range(ps, pe):
            if part[j] <= pivot:
                i += 1
                part[i], part[j] = part[j], part[i]
        part[i + 1], part[pe] = part[pe], part[i + 1]
        return i + 1
    
    if start >= end:
        return None
    
    p = partition(lst, start, end)
    quicksort(lst, start, p - 1)
    quicksort(lst, p + 1, end)
    return lst