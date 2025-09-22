from typing import List, Dict

_passed = 0
_total = 0

def CHECK (msg:str, cond:bool) -> None:
    global _passed
    global _total
    _total += 1
    if cond : _passed += 1
    print ("[{}] {}".format("PASS" if cond else "FAIL", msg))

def linear_search(nums:List[int],target:int) -> int:
    for i, n in enumerate(nums):
        if n == target:
            return i
    return -1

def _demo_linear_search():
    print ("----------------- LINEAR SEARCH -----------------")
    CHECK("Linear Search", linear_search([9,3,6,7,1,5],7) == 3)
    CHECK("Linear Search", linear_search([9,3,6,7,1,5],77) == -1)
    CHECK("Linear Search", linear_search([9],9) == 0)
    CHECK("Linear Search", linear_search([],9) == -1)

def binary_search(a:List[int], target:int) -> int:
    l = 0
    r = len(a) - 1

    while (l <= r):
        m = l + (r-l) // 2
        if (target == a[m]):
            return m
        elif (target > a[m]):
            l = m + 1
        else:
            r = m - 1
    return -1

def _demo_binary_search():
    print ("----------------- BINARY SEARCH -----------------")
    CHECK("Linear Search", binary_search([0, 1, 2, 3, 3, 4, 5, 6, 8], 7) == -1)
    CHECK("Linear Search", binary_search([0, 1, 2, 6, 8], 6) == 3)
    CHECK("Linear Search", binary_search([0, 1, 2, 3, 3, 4, 5, 6, 8], 3) == 4)
    CHECK("Linear Search", binary_search([9],9) == 0)
    CHECK("Linear Search", binary_search([],9) == -1)

def search_insert_position(a:List[int], tgt:int) -> int:
    l = 0
    r = len(a) - 1

    while (l <= r):
        m = l + (r-l)//2
        if tgt == a[m]:
            return m
        elif tgt > a[m]:
            l = m + 1
        else:
            r = m - 1
    return l

def _demo_search_insert_position():
    print ("----------------- SEARCH INSERT POSITION -----------------")
    CHECK("Found target", search_insert_position([1,3,5,6], 5) == 2)
    CHECK("Insert before 3", search_insert_position([1,3,5,6], 2) == 1)
    CHECK("Insert at end", search_insert_position([1,3,5,6], 7) == 4)
    CHECK("Insert at beginning", search_insert_position([1,3,5,6], 0) == 0)

def binary_search_rotated(a:List[int], tgt:int) -> int:
    l = 0
    r = len(a) - 1

    while (l <= r):
        m = l + (r-l)//2
        if (a[m] == tgt):
            return m
        
        if a[l] <= a[m]:
            if (a[l]  <= tgt < a[m]):
                r = m-1
            else:
                l = m+1
        else:
            if (a[m] < tgt <= a[r]):
                l = m+1
            else:
                r = m-1
        
    return -1

def _demo_binary_search_rotated():
    print ("----------------- BINARY SEARCH ROTATED -----------------")
    CHECK("Target 0 in rotated", binary_search_rotated([4,5,6,7,0,1,2], 0) == 4)
    CHECK("Target 3 not found", binary_search_rotated([4,5,6,7,0,1,2], 3) == -1)
    CHECK("Single element found", binary_search_rotated([1], 1) == 0)
    CHECK("Single element not found", binary_search_rotated([1], 0) == -1)
    CHECK("Target 6 in rotated", binary_search_rotated([6,7,8,1,2,3,4,5], 6) == 0)
    CHECK("Target 5 in rotated", binary_search_rotated([6,7,8,1,2,3,4,5], 5) == 7)

def binary_search_min_rotated(a:List[int]) -> int:
    l = 0
    r = len(a)-1

    while (l < r):
        m = l + (r-l)//2
        if (a[m] > a[r]):
            l = m+1
        else:
            r = m
    return a[l]

def _demo_binary_search_min_rotated():
    print ("----------------- BINARY SEARCH MIN ROTATED -----------------")
    CHECK("Standard rotation", binary_search_min_rotated([3,4,5,1,2]) == 1)
    CHECK("Pivot in middle", binary_search_min_rotated([4,5,6,7,0,1,2]) == 0)
    CHECK("Already sorted", binary_search_min_rotated([11,13,15,17]) == 11)
    CHECK("Single element", binary_search_min_rotated([2]) == 2)
    CHECK("Two elements rotated", binary_search_min_rotated([2,1]) == 1)
    CHECK("Two elements sorted", binary_search_min_rotated([1,2]) == 1)
    CHECK("Large rotation", binary_search_min_rotated([30,40,50,10,20]) == 10)
    CHECK("Pivot at end", binary_search_min_rotated([2,3,4,5,1]) == 1)

def median_two_sorted(a:List[int], b:List[int]) -> float:
    c = []
    la = len(a)
    lb = len(b)
    i = j = 0
    while (i<la and j<lb):
        if (a[i] < b[j]):
            c.append(a[i])
            i+=1
        else:
            c.append(b[j])
            j+=1
    c.extend(a[i:])
    c.extend(b[j:])

    print (c)

    n = len(c)
    if (n%2) != 0:
        return float(c[n//2])
    else:
        return (c[n//2-1] + c[n//2])/2.0

def _demo_median_two_sorted():
    #print (median_two_sorted([1,3], [2]))
    CHECK("Odd total length", median_two_sorted([1,3], [2]) == 2.0)
    CHECK("Even total length", median_two_sorted([1,2], [3,4]) == 2.5)
    CHECK("One array empty", median_two_sorted([], [5,6,7,8]) == 6.5)
    CHECK("Duplicates present", median_two_sorted([1,1], [1,2]) == 1.0)
    CHECK("Different sizes", median_two_sorted([3,5,8,9], [1,2,7,10,11,12]) == 7.5)
    CHECK("With negatives", median_two_sorted([-5,3,6], [-2,-1,4,10]) == 3.0)

def _summarize():
    global _passed
    global _total
    print ("------------------------------------------------------")
    print ("PASS:  {}".format(_passed))
    print ("TOTAL: {}".format(_total))
    print ("------------------------------------------------------")

if __name__ == "__main__":
    _demo_linear_search()
    _demo_binary_search()
    _demo_search_insert_position()
    _demo_binary_search_rotated()
    _demo_binary_search_min_rotated()
    _demo_median_two_sorted()
    _summarize()
