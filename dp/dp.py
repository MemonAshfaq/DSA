# ==========================================
# Dynamic Programming Practice
# ==========================================

# ------------------------------
# Problem 1: Climbing Stairs
# ------------------------------

def climb_stairs_bf_up(n: int) -> int:
    # FROM approach
    def dfs(i):
        if i == n: return 1
        if i > n: return 0
        return dfs(i+1) + dfs(i+2)
    return dfs(0)

def climb_stairs_bf_down(n: int) -> int:
    # TO approach
    def dfs(i):
        if i == 0: return 1
        if i < 0: return 0
        return dfs(i-1) + dfs(i-2)
    return dfs(n)

def climb_stairs_memo_up(n: int) -> int:
    memo = {}
    def dfs(i):
        if i == n: return 1
        if i > n: return 0
        if i in memo: return memo[i]
        memo[i] = dfs(i+1) + dfs(i+2)
        return memo[i]
    return dfs(0)

def climb_stairs_memo_down(n: int) -> int:
    memo = {}
    def dfs(i):
        if i == 0: return 1
        if i < 0: return 0
        if i in memo: return memo[i]
        memo[i] = dfs(i-1) + dfs(i-2)
        return memo[i]
    return dfs(n)

def climb_stairs_tab_up(n: int) -> int:
    dp = [0]*(n+1)
    dp[0] = 1 # there is just 1 way to stand/reach ground
    dp[1] = 1 # there is just 1 way to go from ground to step1

    for i in range(2,n+1):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[-1]

def climb_stairs_fib(n: int) -> int:
    if n <= 2: return n
    a, b = 1, 2
    for _ in range(3, n+1):
        c = a+b
        a, b = b, c
    return c

# ------------------------------
# Problem 2: House Robber I
# ------------------------------
def rob_bf_down(nums: list[int]) -> int:
    n = len(nums)
    def dfs(i):
        if i == 0: return nums[0]
        if i == 1: return max(nums[0], nums[1])
        return max(nums[i] + dfs(i-2), dfs(i-1))
    return dfs(n-1)

def rob_bf_up(nums: list[int]) -> int:
    n = len(nums)
    def dfs(i):
        if i >= n: return 0
        return max(nums[i] + dfs(i+2), dfs(i+1))
    return dfs(0)

def rob_memo_down(nums: list[int]) -> int:
    n = len(nums)
    memo = {}
    def dfs(i):
        if i == 0: return nums[0]
        if i == 1: return max(nums[0], nums[1])
        if i in memo: return memo[i]
        memo[i] = max(nums[i] + dfs(i-2), dfs(i-1))
        return memo[i]
    return dfs(n-1)

def rob_memo_up(nums: list[int]) -> int:
    n = len(nums)
    memo = {}
    def dfs(i):
        if i >= n: return 0
        if i in memo: return memo[i]
        memo[i] = max(nums[i] + dfs(i+2), dfs(i+1))
        return memo[i]
    return dfs(0)

def rob_tab_up(nums: int) -> int:
    n = len(nums)

    dp = [0]*n
    dp[0] = nums[0]
    dp[1] = max(nums[0],nums[1])

    for i in range(2,n):
        dp[i] = max(nums[i]+dp[i-2], dp[i-1])
    
    return dp[-1]

def rob_opt(nums: list[int]) -> int:
    n = len(nums)
    if n == 1:
        return nums[0]
    if n == 2:
        return max(nums[0], nums[1])

    dpi_2 = nums[0]                  # dp[i-2]
    dpi_1 = max(nums[0], nums[1])    # dp[i-1]

    for i in range(2, n):
        dpi = max(dpi_1, nums[i] + dpi_2)
        dpi_2 = dpi_1
        dpi_1 = dpi
    
    return dpi

def rob2(nums: list[int]) -> int:
    n = len(nums)
    if n == 1:
        return nums[0]
    if n == 2:
        return max(nums[0], nums[1])

    # Case 1: Exclude last house
    loot1 = rob_opt(nums[:-1])
    # Case 2: Exclude first house
    loot2 = rob_opt(nums[1:])
    
    return max(loot1, loot2)
# ==========================================
# Test Cases
# ==========================================

if __name__ == "__main__":
    print("\n===== Climbing Stairs =====")
    for n in [2, 3, 5, 6]:
        print(f"n={n} → bf_up={climb_stairs_bf_up(n)}, "
              f"bf_down={climb_stairs_bf_down(n)}, "
              f"memo_up={climb_stairs_memo_up(n)}, "
              f"memo_down={climb_stairs_memo_down(n)}, "
              f"tab_up={climb_stairs_tab_up(n)}, "
              f"fib={climb_stairs_fib(n)}")

    print("\n===== House Robber =====")
    testcases = [
        [1,2,3,1],
        [2,7,9,3,1],
        [2,1,1,2]
    ]
    for nums in testcases:
        print(f"nums={nums} → bf_down={rob_bf_down(nums)}, "
              f"bf_up={rob_bf_up(nums)}, "
              f"memo_down={rob_memo_down(nums)}, "
              f"memo_up={rob_memo_up(nums)}",
              f"memo_up={rob_tab_up(nums)}",
              f"rob_opt={rob_opt(nums)}",)

    print("\n===== House Robber II =====")
    testcases2 = [
        [2,3,2],      # Expected 3
        [1,2,3,1],    # Expected 4
        [5,1,1,5],    # Expected 6
        [4,2,3,9],    # Expected 11
        [7],          # Expected 7 (edge case: one house)
        [2,10]        # Expected 10 (edge case: two houses)
    ]
    for nums in testcases2:
        print(f"nums={nums} → rob2={rob2(nums)}")
