def climb_up_stairs_bf(n:int) -> int:
    # from approach
    def dfs(i):
        if (i == n):
            return 1
        if (i > n):
            return 0
        
        return dfs(i+1) + dfs(i+2)
    return dfs(0)

def climb_down_stairs_bf(n:int) -> int:
    # to approach
    def dfs(i):
        if (i == 0):
            return 1
        if (i < 0):
            return 0
        
        return dfs(i-1) + dfs(i-2)
    return dfs(n)

def climb_up_stairs_memo(n:int) -> int:
    # from approach
    memo = {}
    def dfs(i):
        if (i == n):
            return 1
        
        if (i > n):
            return 0
        
        if i in memo:
            return memo[i]
        
        memo[i] = dfs(i+1) + dfs(i+2)
        return memo[i]

    return dfs(0)

def climb_down_stairs_memo(n:int) -> int:
    # to approach
    memo = {}
    def dfs(i):
        if (i == 0):
            return 1
        if (i < 0):
            return 0
        
        if i in memo:
            return memo[i]

        memo[i] = dfs(i-1) + dfs(i-2)
        return memo[i]

    return dfs(n)

def climb_stairs_fib(n:int) -> int:
    if n <= 2: return n
    else:
        a = 1
        b = 2
        for _ in range(3,n+1):
            c = a+b
            a = b
            b = c
    return c
                
total_ways = climb_up_stairs_bf(5)
print (total_ways)

total_ways = climb_down_stairs_bf(5)
print (total_ways)

total_ways = climb_up_stairs_bf(5)
print (total_ways)

total_ways = climb_down_stairs_bf(5)
print (total_ways)

total_ways = climb_stairs_fib(5)
print (total_ways)
