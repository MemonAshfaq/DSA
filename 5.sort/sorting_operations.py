from typing import List
import random

_passed = 0
_total = 0

def CHECK (msg:str, cond:bool) -> None:
    global _passed
    global _total
    _total += 1
    if cond : _passed += 1
    print ("[{}] {}".format("PASS" if cond else "FAIL", msg))

def bubble_sort(a:List[int]) -> List[int]:
    a = a[:] # Copy into a local variable so that it doesn't affect the original array
    for i in range(len(a)):
        swap = False
        for j in range(1,len(a)-i):
            if a[j-1] > a[j]:
                a[j-1],a[j] = a[j], a[j-1]
                swap = True
        if swap == False:
            break #early exit
    return a

def _demo_bubble_sort():
    print ("------------------- Bubble Sort -------------------")
    CHECK("basic unsorted", bubble_sort([0, 1, 2, 3, 3, 4, 8, 6, 5]) == [0, 1, 2, 3, 3, 4, 5, 6, 8])
    CHECK("already sorted", bubble_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5])
    CHECK("reverse order", bubble_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5])
    CHECK("all duplicates", bubble_sort([7, 7, 7, 7]) == [7, 7, 7, 7])
    CHECK("negatives + positives", bubble_sort([3, -1, 2, -5, 0]) == [-5, -1, 0, 2, 3])
    CHECK("empty list", bubble_sort([]) == [])
    CHECK("single element", bubble_sort([42]) == [42])

def insertion_sort(a:List[int]) -> List[int]:
    a = a[:] #shallow copy
    for i in range(len(a)):
        for j in range(i,0,-1):
            if a[j] < a[j-1]:
                a[j], a[j-1] = a[j-1], a[j]
            else:
                break
    return a

def _demo_insertion_sort():
    print ("------------------- Insertion Sort -------------------")
    CHECK("basic unsorted", insertion_sort([0, 1, 2, 3, 3, 4, 8, 6, 5]) == [0, 1, 2, 3, 3, 4, 5, 6, 8])
    CHECK("already sorted", insertion_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5])
    CHECK("reverse order", insertion_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5])
    CHECK("all duplicates", insertion_sort([7, 7, 7, 7]) == [7, 7, 7, 7])
    CHECK("negatives + positives", insertion_sort([3, -1, 2, -5, 0]) == [-5, -1, 0, 2, 3])
    CHECK("empty list", insertion_sort([]) == [])
    CHECK("single element", insertion_sort([42]) == [42])

def selection_sort(a:List[int]) -> List[int]:
    a = a[:]
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if a[j] < a[i]:
                a[i], a[j] = a[j], a[i]
    return a

def _demo_selection_sort():
    print ("------------------- Selection Sort -------------------")
    CHECK("basic unsorted", selection_sort([0, 1, 2, 3, 3, 4, 8, 6, 5]) == [0, 1, 2, 3, 3, 4, 5, 6, 8])
    CHECK("already sorted", selection_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5])
    CHECK("reverse order", selection_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5])
    CHECK("all duplicates", selection_sort([7, 7, 7, 7]) == [7, 7, 7, 7])
    CHECK("negatives + positives", selection_sort([3, -1, 2, -5, 0]) == [-5, -1, 0, 2, 3])
    CHECK("empty list", selection_sort([]) == [])
    CHECK("single element", selection_sort([42]) == [42])

def _merge(left:List[int], right:List[int]):
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

def merge_sort(a:List[int]) -> List[int]:
    if len(a) <= 1:
        return a
    mid = len(a) // 2
    left = merge_sort(a[:mid])
    right = merge_sort(a[mid:])
    return _merge(left, right)

def _demo_merge_sort():
    print ("------------------- Merge Sort -------------------")
    CHECK("basic unsorted", merge_sort([0, 1, 2, 3, 3, 4, 8, 6, 5]) == [0, 1, 2, 3, 3, 4, 5, 6, 8])
    CHECK("already sorted", merge_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5])
    CHECK("reverse order", merge_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5])
    CHECK("all duplicates", merge_sort([7, 7, 7, 7]) == [7, 7, 7, 7])
    CHECK("negatives + positives", merge_sort([3, -1, 2, -5, 0]) == [-5, -1, 0, 2, 3])
    CHECK("empty list", merge_sort([]) == [])
    CHECK("single element", merge_sort([42]) == [42])

def quick_sort(a:List[int]) -> List[int]:
    if len(a) <= 1:
        return a
    
    pivot = a.pop()

    lower = []
    greater = []

    for n in a:
        if n < pivot:
            lower.append(n)
        else:
            greater.append(n)
    
    return(quick_sort(lower) + [pivot] + quick_sort(greater))

def quick_sort_op(a:List[int]) -> List[int]:
    if len(a) <= 1:
        return a
    
    pivot = random.choice(a)

    lower = [x for x in a if x < pivot]
    equal = [x for x in a if x == pivot]
    greater = [x for x in a if x > pivot]

    return(quick_sort_op(lower) + equal + quick_sort_op(greater))

def _partition(a:List[int], low:int, high:int) -> int:
    p = a[low]
    i = low+1
    j = high

    while True:
        while (i <= j and a[i] <= p):
            i += 1
        while (i <= j and a[j] >= p):
            j -= 1
        if (i<=j):
            a[i], a[j] = a[j], a[i]
        else:
            break
    a[low], a[j] = a[j], a[low]
    return j


def quick_sort_inplace(a:List[int],low:int, high:int) -> None:
    if low < high:
        # partition and get pivot
        p = _partition(a, low, high)
        # quick sort the lower part
        quick_sort_inplace(a,low,p-1)
        # quick sort the higher part
        quick_sort_inplace(a,p+1,high)
    return a

def _demo_quick_sort():
    print ("------------------- Quick Sort -------------------")
    CHECK("basic unsorted", quick_sort([0, 1, 2, 3, 3, 4, 8, 6, 5]) == [0, 1, 2, 3, 3, 4, 5, 6, 8])
    CHECK("already sorted", quick_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5])
    CHECK("reverse order", quick_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5])
    CHECK("all duplicates", quick_sort([7, 7, 7, 7]) == [7, 7, 7, 7])
    CHECK("negatives + positives", quick_sort([3, -1, 2, -5, 0]) == [-5, -1, 0, 2, 3])
    CHECK("empty list", quick_sort([]) == [])
    CHECK("single element", quick_sort([42]) == [42])

    print ("------------------- Quick Sort Improved -------------------")
    CHECK("basic unsorted", quick_sort_op([0, 1, 2, 3, 3, 4, 8, 6, 5]) == [0, 1, 2, 3, 3, 4, 5, 6, 8])
    CHECK("already sorted", quick_sort_op([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5])
    CHECK("reverse order", quick_sort_op([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5])
    CHECK("all duplicates", quick_sort_op([7, 7, 7, 7]) == [7, 7, 7, 7])
    CHECK("negatives + positives", quick_sort_op([3, -1, 2, -5, 0]) == [-5, -1, 0, 2, 3])
    CHECK("empty list", quick_sort_op([]) == [])
    CHECK("single element", quick_sort_op([42]) == [42])

    print ("------------------- Quick Sort In-Place -------------------")
    CHECK("basic unsorted", quick_sort_inplace([0, 1, 2, 3, 3, 4, 8, 6, 5],0,8) == [0, 1, 2, 3, 3, 4, 5, 6, 8])
    CHECK("already sorted", quick_sort_inplace([1, 2, 3, 4, 5],0,4) == [1, 2, 3, 4, 5])
    CHECK("reverse order", quick_sort_inplace([5, 4, 3, 2, 1],0,4) == [1, 2, 3, 4, 5])
    CHECK("all duplicates", quick_sort_inplace([7, 7, 7, 7],0,3) == [7, 7, 7, 7])
    CHECK("negatives + positives", quick_sort_inplace([3, -1, 2, -5, 0],0,4) == [-5, -1, 0, 2, 3])
    CHECK("empty list", quick_sort_inplace([],0,-1) == [])
    CHECK("single element", quick_sort_inplace([42],0,0) == [42])

def _summarize():
    global _passed
    global _total
    print ("------------------------------------------------------")
    print ("PASS:  {}".format(_passed))
    print ("TOTAL: {}".format(_total))
    print ("------------------------------------------------------")
    
if __name__ == "__main__":
    _demo_bubble_sort()
    _demo_insertion_sort()
    _demo_selection_sort()
    _demo_merge_sort()
    _demo_quick_sort()
    _summarize()