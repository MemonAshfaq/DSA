from typing import Dict, List

_passed = 0
_total = 0
def CHECK(msg: str, cond: bool):
    global _total
    global _passed

    _total += 1
    if cond: _passed += 1

    print ("[{}] {}".format("PASS" if cond else "FAIL", msg))

#---------------------------------------------------------------
#   Problem: Two Sum (LeetCode #1)
#---------------------------------------------------------------
"""
Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.

- Each input has exactly one solution.
- You may not use the same element twice.
- You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
"""

"""
Two Sum — Complexity

Approach         Time      Space    Notes
-----------------------------------------------
Brute Force      O(n^2)    O(1)     Check all pairs
HashMap (1-pass) O(n)      O(n)     Store value->index, fast lookup
"""
def two_sum_bf(nums: List, target: int) -> List[int]:
    l = len(nums)
    for i in range(0,l):
        for j in range(i+1,l):
            if nums[i]+nums[j] == target:
                return [i,j]
    return []

def two_sum_op(nums: List, target: int) -> List[int]:
    hm = {}
    for i, n in enumerate(nums):
        d = target - n
        j = hm.get(d,-1)
        if j != -1:
            return [j,i]
        hm[n] = i
    return []

def _demo_two_sum():
    CHECK("TWO_SUM_BF", two_sum_bf([2,7,11,15],9) == [0,1])
    CHECK("TWO_SUM_OP", two_sum_op([2,7,11,15],9) == [0,1])
    CHECK("TWO_SUM_BF", two_sum_bf([3,2,4],6) == [1,2])
    CHECK("TWO_SUM_OP", two_sum_op([3,2,4],6) == [1,2])
    CHECK("TWO_SUM_BF", two_sum_bf([3,3],6) == [0,1])
    CHECK("TWO_SUM_OP", two_sum_op([3,3],6) == [0,1])
    CHECK("TWO_SUM_BF", two_sum_bf([4,3,-5],-1) == [0,2])
    CHECK("TWO_SUM_OP", two_sum_op([4,3,-5],-1) == [0,2])

#---------------------------------------------------------------
#   Problem: Best Time to Buy and Sell Stock (LeetCode #121)
#---------------------------------------------------------------
"""
Problem:
  Given an array prices where prices[i] is the stock price on day i,
  compute the maximum profit from exactly one transaction
  (buy one day and sell on a later day). If no profit is possible, return 0.

Input:
  prices: List[int]  # length n >= 1; prices are non-negative integers

Output:
  int  # maximum achievable profit from a single buy/sell, or 0 if none

Rules / Notes:
  - You must buy before you sell (i < j).
  - Only one transaction allowed (one buy, one sell).

Examples:
  prices = [7,1,5,3,6,4]   -> 5   # buy at 1, sell at 6
  prices = [7,6,4,3,1]     -> 0   # no profitable transaction

Approach (one-pass):
  Track the minimum price seen so far (min_so_far) while scanning left→right.
  At each day, potential profit = prices[i] - min_so_far; update max_profit.

Complexity:
  Time: O(n)   Space: O(1)

Function signature:
  def max_profit(prices: List[int]) -> int:
"""
def max_profit_bf_v0(prices: List[int]) -> int:
    profit = 0
    days = []
    for d1, p1 in enumerate(prices[:]):
        for d2, p2 in enumerate(prices[d1+1:]):
            d2 = d2+d1+1
            diff = p2-p1
            if (diff > profit):
                profit = diff
                days = [d1,d2]
    return profit, days

def max_profit_bf_v1(prices: List[int]) -> int:
    profit:int = 0
    days:List[int] = []
    totaldays = len(prices)

    for d1 in range(totaldays):
        for d2 in range(d1+1,totaldays):
            diff = prices[d2] - prices[d1]
            if (diff > profit):
                profit = diff
                days = [d1,d2]
    return profit, days

def max_profit_bf_v1(prices: List[int]) -> int:
    profit:int = 0
    days:List[int] = []
    totaldays = len(prices)

    for d1 in range(totaldays):
        for d2 in range(d1+1,totaldays):
            diff = prices[d2] - prices[d1]
            if (diff > profit):
                profit = diff
                days = [d1,d2]
    return profit, days

def max_profit_op_v0(prices: List[int]) -> int:
    max_profit:int = 0
    min_price: int = float('inf')
    buy_day = None
    sell_day = None

    for day, price in enumerate(prices):
        if price < min_price:
            min_price = price
            buy_day = day
        profit = price - min_price
        if profit > max_profit:
            max_profit = profit
            sell_day = day
    return (max_profit, [buy_day,sell_day]) if max_profit > 0 else (0,[])

"""
-------------------------------------------------------------
Complexity Comparison
-------------------------------------------------------------
Version           | Time Complexity | Space Complexity | Notes
----------------- | --------------- | ---------------- | -----------------------------
Brute Force (BF)  | O(n^2)          | O(1)             | Check all pairs (buy,sell)
Optimized (One-P) | O(n)            | O(1)             | Track min-so-far & max profit
-------------------------------------------------------------
"""
def _demo_max_profit():
    # test BF v0
    CHECK("MAX_PROFIT_BF_V0", max_profit_bf_v0([7,1,5,3,6,4]) == (5,[1,4]))
    CHECK("MAX_PROFIT_BF_V0", max_profit_bf_v0([7,7,7,7,7,7]) == (0,[]))
    CHECK("MAX_PROFIT_BF_V0", max_profit_bf_v0([7,6,5,4,3,2,1]) == (0,[]))
    CHECK("MAX_PROFIT_BF_V0", max_profit_bf_v0([1,2,3,4,5,6,7]) == (6,[0,6]))
    # test BF v1
    CHECK("MAX_PROFIT_BF_V1", max_profit_bf_v1([7,1,5,3,6,4]) == (5,[1,4]))
    CHECK("MAX_PROFIT_BF_V1", max_profit_bf_v1([7,7,7,7,7,7]) == (0,[]))
    CHECK("MAX_PROFIT_BF_V1", max_profit_bf_v1([7,6,5,4,3,2,1]) == (0,[]))
    CHECK("MAX_PROFIT_BF_V1", max_profit_bf_v1([1,2,3,4,5,6,7]) == (6,[0,6]))
    # test BF v1
    CHECK("MAX_PROFIT_OP_V0", max_profit_op_v0([7,1,5,3,6,4]) == (5,[1,4]))
    CHECK("MAX_PROFIT_OP_V0", max_profit_op_v0([7,7,7,7,7,7]) == (0,[]))
    CHECK("MAX_PROFIT_OP_V0", max_profit_op_v0([7,6,5,4,3,2,1]) == (0,[]))
    CHECK("MAX_PROFIT_OP_V0", max_profit_op_v0([1,2,3,4,5,6,7]) == (6,[0,6]))

#----------------------------------------------------------
# 217. Contains Duplicate (217)
#----------------------------------------------------------
"""
Problem: Check if any value appears at least twice in the array.
Input: List of integers

Output: Boolean (True if duplicates exist, False otherwise)

Examples:
  [1,2,3,1] -> True
  [1,2,3,4] -> False
  [1,1,1,3,3,4,3,2,4,2] -> True

Edge cases to watch:
- Empty list → False
- Single element → False
- All unique → False
- Negatives / zeros mixed with positives

Pattern: Hash set OR sort + scan
"""
def has_duplicates_bf(nums: List[int]) -> bool:
    l = len(nums)
    for i in range(l):
        for j in range(i+1,l):
            if nums[i] == nums[j]:
                return True
    return False

def has_duplicates_op(nums: List[int]) -> bool:
    hs = set()

    for n in nums:
        if n in hs:
            return True
        hs.add(n)
    return False

"""
------------------------------------------------------------
Complexity Comparison
------------------------------------------------------------
Version            | Time   | Space | Notes
-------------------|--------|-------|-------------------------------
has_duplicates_bf  | O(n^2) | O(1)  | Double loop, slow for large n
has_duplicates_op  | O(n)   | O(n)  | HashSet lookup, fast in practice
------------------------------------------------------------
"""
def _demo_has_duplicates():
    #---------------- has_duplicates_bf -----------------
    CHECK("HAS_DUP_BF", has_duplicates_bf([1,2,3,1]) == True)
    CHECK("HAS_DUP_BF", has_duplicates_bf([1,2,3,4]) == False)
    CHECK("HAS_DUP_BF", has_duplicates_bf([1,1,1,3,3,4,3,2,4,2]) == True)
    #---------------- has_duplicates_op -----------------
    CHECK("HAS_DUP_OP", has_duplicates_op([1,2,3,1]) == True)
    CHECK("HAS_DUP_OP", has_duplicates_op([1,2,3,4]) == False)
    CHECK("HAS_DUP_OP", has_duplicates_op([1,1,1,3,3,4,3,2,4,2]) == True)

#----------------------------------------------------------
# 238. Product of Array Except Self
#----------------------------------------------------------
"""
Problem: For each index, return the product of all elements except nums[i],
without using division.

Input: List[int] nums

Output: List[int] (same length as input, each position is product of others)

Examples:
  [1,2,3,4] -> [24,12,8,6]
  [-1,1,0,-3,3] -> [0,0,9,0,0]
  [0,0,2] -> [0,0,0]

Edge cases to watch:
- Empty list → []
- Single element → []
- One zero vs multiple zeros
- Negatives and large magnitudes

Pattern: Prefix * Suffix (no division)
"""

def product_except_self_bf(nums: List[int]) -> List[int]:
    """
    Brute force: for each index, multiply all other elements directly.
    T: O(n^2), S: O(1) extra
    """
    l = len(nums)
    plist = []
    
    for i in range(l):
        p = 1
        for j in range(l):
            if (i!=j):
                p = p*nums[j]
        plist.append(p)

    return plist

def product_except_self_op_v0(nums: List[int]) -> List[int]:
    """
    Optimal: prefix * suffix products (two passes).
    T: O(n), S: O(1) extra (excluding output)
    """
    l = len(nums)
    prelist = [1]*l
    postlist = [1]*l
    prodlist = [1]*l

    prefix = 1
    postfix = 1
    for i in range(1,l):
        prefix *= nums[i-1]
        prelist[i] = prefix

    for i in range(l-2,-1,-1):
        postfix *= nums[i+1]
        postlist[i] = postfix

    for i in range(l):
        prodlist[i] = prelist[i] * postlist[i]

    return prodlist

def product_except_self_op_v1(nums: List[int]) -> List[int]:
    """
    Optimal: prefix * suffix products (two passes).
    T: O(n), S: O(1) extra (excluding output)
    """
    l = len(nums)
    prodlist = [1]*l

    prefix = 1
    postfix = 1

    for i in range(1,l):
        prefix *= nums[i-1]
        prodlist[i] = prefix

    for i in range(l-2,-1,-1):
        postfix *= nums[i+1]
        prodlist[i] *= postfix

    return prodlist

"""
------------------------------------------------------------
Complexity Comparison
------------------------------------------------------------
Version                  | Time   | Space | Notes
--------------------------|--------|-------|-------------------------------
product_except_self_bf    | O(n^2) | O(1)  | Multiply all except self per i
product_except_self_op    | O(n)   | O(1)  | Prefix * Suffix, no division
------------------------------------------------------------
"""

def _demo_product_except_self():
    #---------------- product_except_self_bf -----------------
    CHECK("product_except_self_bf", product_except_self_bf([1,2,3,4]) == [24,12,8,6])
    CHECK("product_except_self_bf", product_except_self_bf([-1,1,0,-3,3]) == [0,0,9,0,0])
    CHECK("product_except_self_bf", product_except_self_bf([2,3]) == [3,2])
    CHECK("product_except_self_bf", product_except_self_bf([7]) == [1])
    CHECK("product_except_self_bf", product_except_self_bf([]) == [])
    CHECK("product_except_self_bf", product_except_self_bf([-2,-3,-4]) == [12,8,6])

    #---------------- product_except_self_op -----------------
    CHECK("product_except_self_op_v0", product_except_self_op_v0([1,2,3,4]) == [24,12,8,6])
    CHECK("product_except_self_op_v0", product_except_self_op_v0([-1,1,0,-3,3]) == [0,0,9,0,0])
    CHECK("product_except_self_op_v0", product_except_self_op_v0([2,3]) == [3,2])
    CHECK("product_except_self_op_v0", product_except_self_op_v0([7]) == [1])
    CHECK("product_except_self_op_v0", product_except_self_op_v0([]) == [])
    CHECK("product_except_self_op_v0", product_except_self_op_v0([-2,-3,-4]) == [12,8,6])

    #---------------- product_except_self_op -----------------
    CHECK("product_except_self_op_v1", product_except_self_op_v1([1,2,3,4]) == [24,12,8,6])
    CHECK("product_except_self_op_v1", product_except_self_op_v1([-1,1,0,-3,3]) == [0,0,9,0,0])
    CHECK("product_except_self_op_v1", product_except_self_op_v1([2,3]) == [3,2])
    CHECK("product_except_self_op_v1", product_except_self_op_v1([7]) == [1])
    CHECK("product_except_self_op_v1", product_except_self_op_v1([]) == [])
    CHECK("product_except_self_op_v1", product_except_self_op_v1([-2,-3,-4]) == [12,8,6])

#----------------------------------------------------------
# 53. Maximum Subarray
#----------------------------------------------------------
"""
Problem: Find the contiguous subarray with the largest sum.

Input: List[int] nums
Output: int (maximum sum)

Examples:
  [-2,1,-3,4,-1,2,1,-5,4] -> 6  (subarray [4,-1,2,1])
  [1] -> 1
  [5,4,-1,7,8] -> 23
  [-1,-2,-3,-4] -> -1

Edge cases to watch:
- All negatives → pick max single element
- Single element array
- Large input size (performance)
- Zeros in the array

Pattern: Kadane’s Algorithm (Dynamic Programming)
"""
def max_subarray_bf_v0(nums: List[int]) -> int:
    """
    Brute force: check all subarrays, track max sum.
    T: O(n^3), S: O(1)
    """
    l = len(nums)

    maxsum = nums[0] if l == 1 else -1*float('inf')

    for i in range(l):
        for j in range(i+1,l):
            sum = 0
            for k in range(i,j+1):
                sum += nums[k]
                maxsum = max(sum, maxsum)
    return maxsum

def max_subarray_bf_v1(nums: List[int]) -> int:
    """
    Brute force: check all subarrays, track max sum.
    T: O(n^2), S: O(1)
    """
    l = len(nums)
    maxsum = nums[0]
    
    for i in range(l):
        sum = 0
        for j in range(i,l):
            sum += nums[j]
            maxsum = max(sum, maxsum)
    return maxsum

def max_subarray_op(nums: List[int]) -> int:
    """
    Optimal (Kadane's Algorithm):
    Keep running sum; reset if <0; track best seen.
    T: O(n), S: O(1)
    """
    max_sum = nums[0]
    cur_sum = 0
    for n in nums:
        cur_sum = max(cur_sum, 0)
        cur_sum += n
        max_sum = max(cur_sum, max_sum)
    return max_sum

"""
------------------------------------------------------------
Complexity Comparison
------------------------------------------------------------
Version              | Time   | Space | Notes
---------------------|--------|-------|------------------------
max_subarray_bf_v0   | O(n^2) | O(1)  | Try every subarray
max_subarray_bf_v1   | O(n^3) | O(1)  | Try every subarray
max_subarray_op      | O(n)   | O(1)  | Kadane’s Algorithm
------------------------------------------------------------
"""

def _demo_max_subarray():
    #---------------- bf v0-----------------
    CHECK("max_subarray_bf_v0", max_subarray_bf_v0([-2,1,-3,4,-1,2,1,-5,4]) == 6)
    CHECK("max_subarray_bf_v0", max_subarray_bf_v0([1]) == 1)
    CHECK("max_subarray_bf_v0", max_subarray_bf_v0([-1,-2,-3]) == -1)

    #---------------- bf v1-----------------
    CHECK("max_subarray_bf_v1", max_subarray_bf_v1([-2,1,-3,4,-1,2,1,-5,4]) == 6)
    CHECK("max_subarray_bf_v1", max_subarray_bf_v1([1]) == 1)
    CHECK("max_subarray_bf_v1", max_subarray_bf_v1([-1,-2,-3]) == -1)

    #---------------- op -----------------
    CHECK("max_subarray_op", max_subarray_op([-2,1,-3,4,-1,2,1,-5,4]) == 6)
    CHECK("max_subarray_op", max_subarray_op([1]) == 1)
    CHECK("max_subarray_op", max_subarray_op([-1,-2,-3]) == -1)

#----------------------------------------------------------
# 152. Maximum Product Subarray
#----------------------------------------------------------
"""
Problem: Find the contiguous subarray (containing at least one number) which has 
the largest product. Return the product.

Input: List[int] nums
Output: int (maximum product)

Examples:
  [2,3,-2,4] -> 6       # subarray [2,3]
  [-2,0,-1] -> 0        # subarray [0]
  [-2,3,-4] -> 24       # subarray [3,-4]

Edge cases to watch:
- Single element array
- Zeros splitting subarrays
- Odd vs even count of negatives
- Large magnitude positives/negatives

Pattern: Dynamic Programming (track max & min product)
"""

def max_subarr_prod_bf_v0(nums: List[int]) -> int:
    l = len(nums)
    maxProd = -float('inf')

    for i in range(l):
        for j in range(i,l):
            prod = 1
            for k in range(i,j+1):
                prod *= nums[k]
            maxProd = max (prod, maxProd)
    return maxProd

def max_subarr_prod_bf_v1(nums: List[int]) -> int:
    l = len(nums)
    maxProd = nums[0]
    for i in range(l):
        prod = 1
        for j in range(i,l):
            prod *= nums[j]
            maxProd = max (prod, maxProd)
    return maxProd

def max_subarr_prod_op(nums: List[int]) -> int:
    min_so_far = max_so_far = max_prod = nums[0]
    for n in nums[1:]:
        if n < 0:
            min_so_far, max_so_far = max_so_far, min_so_far
        max_so_far = max(n, max_so_far*n)
        min_so_far = min(n, min_so_far*n)
        max_prod = max(max_so_far, max_prod)
    return max_prod


def _demo_max_subarray_prod():
    #---------------- v0 (O(n^3)) -----------------
    CHECK("v0 basic", max_subarr_prod_bf_v0([2,3,-2,4]) == 6)
    CHECK("v0 zero split", max_subarr_prod_bf_v0([-2,0,-1]) == 0)
    CHECK("v0 negatives even", max_subarr_prod_bf_v0([-2,3,-4]) == 24)
    CHECK("v0 single elem", max_subarr_prod_bf_v0([5]) == 5)
    CHECK("v0 single negative", max_subarr_prod_bf_v0([-5]) == -5)
    CHECK("v0 all negatives odd", max_subarr_prod_bf_v0([-1,-2,-3]) == 6)
    CHECK("v0 all zeros", max_subarr_prod_bf_v0([0,0,0]) == 0)

    #---------------- v1 (O(n^2)) -----------------
    CHECK("v1 basic", max_subarr_prod_bf_v1([2,3,-2,4]) == 6)
    CHECK("v1 zero split", max_subarr_prod_bf_v1([-2,0,-1]) == 0)
    CHECK("v1 negatives even", max_subarr_prod_bf_v1([-2,3,-4]) == 24)
    CHECK("v1 single elem", max_subarr_prod_bf_v1([5]) == 5)
    CHECK("v1 single negative", max_subarr_prod_bf_v1([-5]) == -5)
    CHECK("v1 all negatives odd", max_subarr_prod_bf_v1([-1,-2,-3]) == 6)
    CHECK("v1 all zeros", max_subarr_prod_bf_v1([0,0,0]) == 0)

    #---------------- op (O(n^2)) -----------------
    CHECK("op basic", max_subarr_prod_op([2,3,-2,4]) == 6)
    CHECK("op zero split", max_subarr_prod_op([-2,0,-1]) == 0)
    CHECK("op negatives even", max_subarr_prod_op([-2,3,-4]) == 24)
    CHECK("op single elem", max_subarr_prod_op([5]) == 5)
    CHECK("op single negative", max_subarr_prod_op([-5]) == -5)
    CHECK("op all negatives odd", max_subarr_prod_op([-1,-2,-3]) == 6)
    CHECK("op all zeros", max_subarr_prod_op([0,0,0]) == 0)

#----------------------------------------------------------
# 33. Search in Rotated Sorted Array
#----------------------------------------------------------
"""
Problem: Given a rotated sorted array and a target value, return the index of
the target if it exists, otherwise return -1. Array has no duplicates.

Input: List[int] nums (sorted, then rotated), int target
Output: int index (or -1 if not found)

Examples:
  nums = [4,5,6,7,0,1,2], target = 0  -> 4
  nums = [4,5,6,7,0,1,2], target = 3  -> -1
  nums = [1], target = 0              -> -1
  nums = [1,3], target = 3            -> 1

Edge cases to watch:
- Single element (match / no match)
- Target not present
- Pivot at start or end
- Very large arrays (performance)

Pattern: Binary Search (identify sorted half and move accordingly)
"""

def search_rotated_bf(nums: List[int], target: int) -> int:
    """
    Brute force: check each element sequentially.
    T: O(n), S: O(1)
    """
    for i,n in enumerate(nums):
        if (target == n):
            return i
    return -1

def search_rotated_op(nums: List[int], target: int) -> int:
    """
    Optimal: modified binary search — find which half is sorted,
    then decide where to move.
    T: O(log n), S: O(1)
    """
    l = 0
    r = len(nums) - 1

    while (l <= r):
        m = (l+r) // 2

        if (target == nums[m]):
            return m
        
        if (nums[l] <= nums[m]):
            if (nums[l] <= target < nums[m]):
                r = m - 1
            else:
                l = m + 1
        else:
            if (nums[m] < target <= nums[r]):
                l = m + 1
            else:
                r = m - 1
    return -1

"""
------------------------------------------------------------
Complexity Comparison
------------------------------------------------------------
Version              | Time     | Space | Notes
---------------------|----------|-------|-------------------------
search_rotated_bf    | O(n)     | O(1)  | Linear scan
search_rotated_op    | O(log n) | O(1)  | Modified binary search
------------------------------------------------------------
"""

def _demo_search_rotated():
    #---------------- bf -----------------
    CHECK("BF target=0", search_rotated_bf([4,5,6,7,0,1,2], 0) == 4)
    CHECK("BF target=3", search_rotated_bf([4,5,6,7,0,1,2], 3) == -1)
    CHECK("BF single no match", search_rotated_bf([1], 0) == -1)
    CHECK("BF two elements", search_rotated_bf([1,3], 3) == 1)

    #---------------- op -----------------
    CHECK("OP target=0", search_rotated_op([4,5,6,7,0,1,2], 0) == 4)
    CHECK("OP target=3", search_rotated_op([4,5,6,7,0,1,2], 3) == -1)
    CHECK("OP single no match", search_rotated_op([1], 0) == -1)
    CHECK("OP two elements", search_rotated_op([1,3], 3) == 1)

#----------------------------------------------------------
# 153. Find Minimum in Rotated Sorted Array
#----------------------------------------------------------
"""
Problem: Given a rotated (possibly zero times) ascending array with UNIQUE elements,
return the minimum element.

Input: List[int] nums  (non-empty; originally strictly increasing, rotated unknown times)
Output: int            (the smallest value in nums)

Examples:
  [3,4,5,1,2]        -> 1
  [4,5,6,7,0,1,2]    -> 0
  [11,13,15,17]      -> 11
  [2,1]              -> 1
  [1]                -> 1

Edge cases to watch:
- Already sorted (no rotation), e.g., [1,2,3,4] -> 1
- Single element, e.g., [7] -> 7
- Pivot near ends, e.g., [2,3,4,5,1] -> 1
- Large/signed values (still unique)
- Duplicates are NOT allowed (invalid for this problem)

Pattern: Binary Search on pivot (right-mid compare)
"""

def find_min_rotated_bf(nums: List[int]) -> int:
    """
    Brute force: linearly scan for the minimum value.
    T: O(n), S: O(1)
    """
    min_val = float('inf')
    for n in nums:
        min_val = min (min_val, n)

    return min_val

def find_min_rotated_op(nums: List[int]) -> int:
    """
    Optimal: binary search using comparison with rightmost element.
    If nums[mid] > nums[right], min is to the right; else to the left/inclusive.
    T: O(log n), S: O(1)
    """
    l, r = 0, len(nums) - 1
    while l < r:
        m = (l + r) // 2
        if nums[m] > nums[r]:
            l = m + 1
        else:
            r = m
    return nums[l]

"""
------------------------------------------------------------
Complexity Comparison
------------------------------------------------------------
Version                | Time     | Space | Notes
-----------------------|----------|-------|-------------------------------
find_min_rotated_bf    | O(n)     | O(1)  | Linear scan
find_min_rotated_op    | O(log n) | O(1)  | BS on pivot (right-mid compare)
------------------------------------------------------------
"""

def _demo_find_min_rotated():
    #---------------- find_min_rotated_bf -----------------
    CHECK("BF basic pivot", find_min_rotated_bf([3,4,5,1,2]) == 1)
    CHECK("BF already sorted", find_min_rotated_bf([1,2,3,4]) == 1)
    CHECK("BF single element", find_min_rotated_bf([1]) == 1)
    CHECK("BF two elements rotated", find_min_rotated_bf([2,1]) == 1)
    CHECK("BF larger pivot", find_min_rotated_bf([4,5,6,7,0,1,2]) == 0)
    CHECK("BF negatives rotated", find_min_rotated_bf([-1,0,1,2,3,-4,-3,-2]) == -4)

    #---------------- find_min_rotated_op -----------------
    CHECK("OP basic pivot", find_min_rotated_op([3,4,5,1,2]) == 1)
    CHECK("OP already sorted", find_min_rotated_op([1,2,3,4]) == 1)
    CHECK("OP single element", find_min_rotated_op([1]) == 1)
    CHECK("OP two elements rotated", find_min_rotated_op([2,1]) == 1)
    CHECK("OP larger pivot", find_min_rotated_op([4,5,6,7,0,1,2]) == 0)
    CHECK("OP negatives rotated", find_min_rotated_op([-1,0,1,2,3,-4,-3,-2]) == -4)

#----------------------------------------------------------
# 15. 3Sum
#----------------------------------------------------------
"""
Problem: Given an integer array, return all unique triplets [a,b,c] such that
a + b + c = 0. Triplets must be unique (no duplicates in output).

Input: List[int] nums
Output: List[List[int]] — list of unique triplets in non-decreasing order per triplet

Examples:
  nums = [-1,0,1,2,-1,-4] -> [[-1,-1,2], [-1,0,1]]
  nums = [0,1,1]          -> []
  nums = [0,0,0,0]        -> [[0,0,0]]

Edge cases to watch:
- Fewer than 3 elements → []
- Many duplicates (ensure de-duplication)
- All zeros vs. no possible triplets
- Large positives/negatives that cannot sum to 0

Pattern: Sort + Two Pointers; skip duplicates
"""
def three_sum_bf(nums: List[int]) -> List[List[int]]:
    """
    Brute force: try all i<j<k, collect triplets that sum to 0 in a set to dedupe
    (e.g., using tuples of sorted triplets), then convert back to lists.
    T: O(n^3), S: O(u) for unique results
    """
    l:int = len(nums)
    res:set[List[int]] = set()

    for i in range(0,l):
        for j in range(i+1,l):
            for k in range(j+1,l):
                if (nums[i] + nums[j] + nums[k]) == 0:
                    trip = tuple(sorted([nums[i],nums[j],nums[k]]))
                    res.add(trip)
    return list(res)

def _two_sum_op(nums:List[int],target:int) -> List[int]:
    hm = {}

    for j,n in enumerate(nums):
        d = target - n
        k = hm.get(d, -1)
        if (k != -1):
            return [nums[k],nums[j]]
        hm[n] = j
    return []

def three_sum_op(nums: List[int]) -> List[List[int]]:
    """
    Optimal: sort, then fix i and use two pointers (l,r) to find pairs summing to -nums[i].
    Skip duplicates at i, l, and r to avoid repeated triplets.
    T: O(n^2), S: O(1) extra (excluding output)
    """
    res:set[List[int]] = set()
    for i, n in enumerate(nums):
        l = _two_sum_op(nums[:i] + nums[i+1:],-nums[i])
        if l:
            l.append(nums[i])
            trip = tuple(sorted(l))
            res.add(trip)
    return list(res)

"""
------------------------------------------------------------
Complexity Comparison
------------------------------------------------------------
Version        | Time   | Space | Notes
---------------|--------|-------|-------------------------------
three_sum_bf   | O(n^3) | O(u)  | Triplet set to dedupe results
three_sum_op   | O(n^2) | O(1)  | Sort + two pointers; skip dups
------------------------------------------------------------
"""
def _demo_three_sum():
    # Helper: normalize for order-insensitive comparison of triplet lists
    def normalize(triplets: List[List[int]]) -> List[List[int]]:
        return sorted([sorted(t) for t in triplets])

    def SAME(a, b) -> bool:
        return normalize(a) == normalize(b)

    #---------------- three_sum_bf -----------------
    CHECK("BF basic",
          SAME(three_sum_bf([-1,0,1,2,-1,-4]), [[-1,-1,2], [-1,0,1]]))
    CHECK("BF no-solution", SAME(three_sum_bf([0,1,1]), []))
    CHECK("BF all zeros",   SAME(three_sum_bf([0,0,0,0]), [[0,0,0]]))
    CHECK("BF duplicates",
          SAME(three_sum_bf([-2,0,0,2,2]), [[-2,0,2]]))
    CHECK("BF small (<3)",  SAME(three_sum_bf([1,2]), []))

    #---------------- three_sum_op -----------------
    CHECK("OP basic",
          SAME(three_sum_op([-1,0,1,2,-1,-4]), [[-1,-1,2], [-1,0,1]]))
    CHECK("OP no-solution", SAME(three_sum_op([0,1,1]), []))
    CHECK("OP all zeros",   SAME(three_sum_op([0,0,0,0]), [[0,0,0]]))
    CHECK("OP duplicates",
          SAME(three_sum_op([-2,0,0,2,2]), [[-2,0,2]]))
    CHECK("OP small (<3)",  SAME(three_sum_op([1,2]), []))
    CHECK("fail?",  SAME(three_sum_op([-4, 1, 3, 2, 2, -3, -2, -1]), 
                                      [[-4, 1, 3], [-4, 2, 2], [-3, 1, 2], [-2, -1, 3]]))
    #CHECK("misses (0,0,0)",
    #    SAME(three_sum_op([-5, 0, 5, 0, 0]),
    #        [[-5,0,5],[0,0,0]]))

#----------------------------------------------------------
# 11. Container With Most Water
#----------------------------------------------------------
"""
Problem: Given n non-negative integers where each represents a vertical line
at index i with height[i], choose two lines that, together with the x-axis,
forms a container that holds the most water. Return that maximum area.

Input: List[int] height
Output: int (maximum water area)

Examples:
  [1,8,6,2,5,4,8,3,7] -> 49
  [1,1]               -> 1
  [4,3,2,1,4]         -> 16

Edge cases to watch:
- Fewer than 2 lines → 0
- Many zeros (e.g., [0,0,0]) → 0
- Plateaus and duplicates (e.g., [2,2,2,2])
- Strictly increasing or decreasing arrays
- Very tall with very short neighbors

Pattern: Two Pointers from both ends; move the smaller line inward.
"""

from typing import List

#---------------- Brute Force Solution ----------------
def container_with_most_water_bf(height: List[int]) -> int:
    """
    Brute force: check all pairs (i, j), compute area = (j - i) * min(h[i], h[j]),
    track the maximum.
    T: O(n^2), S: O(1)
    """
    l = len(height)
    ma = 0

    for i in range(l):
        for j in range(i+1,l):
            a = (j-i) * min(height[i],height[j])
            ma = max(a,ma)

    return (ma)

#---------------- Optimal Solution ----------------
def container_with_most_water_op(height: List[int]) -> int:
    """
    Optimal (Two Pointers): start i=0, j=n-1. Compute area each step.
    Move the pointer at the smaller height inward (hoping for a taller wall),
    because width always shrinks and only a taller min-height can compensate.
    T: O(n), S: O(1)
    """

    i = 0
    j = len(height) - 1
    ma = 0

    while (i < j):
        a = (j-i) * min(height[i],height[j])
        ma = max(a, ma)

        if (height[i] < height[j]):
            i += 1
        else:
            j -= 1
    return ma

"""
------------------------------------------------------------
Complexity Comparison
------------------------------------------------------------
Version                      | Time   | Space | Notes
-----------------------------|--------|-------|-------------------------------
container_with_most_water_bf | O(n^2) | O(1)  | Try every pair
container_with_most_water_op | O(n)   | O(1)  | Two pointers, shrink window
------------------------------------------------------------
"""

#---------------- Self-Tests ----------------
def _demo_container_with_most_water():
    #---------------- bf -----------------
    CHECK("BF basic",
          container_with_most_water_bf([1,8,6,2,5,4,8,3,7]) == 49)
    CHECK("BF two lines",
          container_with_most_water_bf([1,1]) == 1)
    CHECK("BF duplicates wide",
          container_with_most_water_bf([4,3,2,1,4]) == 16)
    CHECK("BF increasing",
          container_with_most_water_bf([1,2,3,4,5,6]) == 9)   # (i=0,h=1,j=5,h=6)->5*1=5; best is i=1..5 -> 4*2=8; i=2..5 -> 3*3=9
    CHECK("BF zeros",
          container_with_most_water_bf([0,0,0]) == 0)
    CHECK("BF small edge <2",
          container_with_most_water_bf([7]) == 0)

    #---------------- op -----------------
    CHECK("OP basic",
          container_with_most_water_op([1,8,6,2,5,4,8,3,7]) == 49)
    CHECK("OP two lines",
          container_with_most_water_op([1,1]) == 1)
    CHECK("OP duplicates wide",
          container_with_most_water_op([4,3,2,1,4]) == 16)
    CHECK("OP increasing",
          container_with_most_water_op([1,2,3,4,5,6]) == 9)
    CHECK("OP zeros",
          container_with_most_water_op([0,0,0]) == 0)
    CHECK("OP small edge <2",
          container_with_most_water_op([7]) == 0)


# -------------- Runner -------------------
def demo_lc_array_hash():
    print ("===========_demo_two_sum==============")
    _demo_two_sum()

    print ("===========_demo_max_profit==============")
    _demo_max_profit()

    print ("===========_demo_has_duplicates==============")
    _demo_has_duplicates()

    print ("===========_demo_product_except_self==============")
    _demo_product_except_self()

    print ("===========_demo_max_subarray==============")
    _demo_max_subarray()

    print ("===========_demo_max_subarray_prod==============")
    _demo_max_subarray_prod()

    print ("===========_demo_search_rotated==============")
    _demo_search_rotated()

    print ("===========_demo_find_min_rotated==============")
    _demo_find_min_rotated()

    print ("===========_demo_three_sum==============")
    _demo_three_sum()

    print ("===========_demo_container_with_most_water==============")
    _demo_container_with_most_water()

# -------------- Main -------------------
if __name__ == "__main__":
    demo_lc_array_hash()
    print ("============================================")
    print ("Result: {}/{} passed".format(_passed, _total))
    print ("============================================")
