import sys

# Increase recursion depth just in case
sys.setrecursionlimit(2000)

def solve_greedy(n, prices):
    """
    Optimized solution for when k is effectively infinite (k >= n/2).
    We simply sum up all positive price differences.
    """
    max_profit = 0
    for i in range(1, n):
        if prices[i] > prices[i-1]:
            max_profit += prices[i] - prices[i-1]
    return max_profit

def solve_dp(n, k, prices):
    """
    Dynamic Programming solution for limited transactions.
    Time: O(n*k), Space: O(k)
    """
    if n <= 1 or k == 0:
        return 0
        
    # buy[i] = max profit after buying the i-th stock
    # sell[i] = max profit after selling the i-th stock (completing i transactions)
    
    # Initialize buy array to -infinity because buying costs money
    buy = [-float('inf')] * (k + 1)
    # Initialize sell array to 0
    sell = [0] * (k + 1)
    
    for p in prices:
        for i in range(1, k + 1):
            # Update buy[i]: 
            # Either keep holding from before, OR buy now using profit from previous transaction (sell[i-1])
            buy[i] = max(buy[i], sell[i-1] - p)
            
            # Update sell[i]:
            # Either keep not holding, OR sell now using the stock we bought (buy[i])
            sell[i] = max(sell[i], buy[i] + p)
            
    return sell[k]

def solve():
    # Read all input at once
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    iterator = iter(input_data)
    
    try:
        # Parse number of test cases
        T_str = next(iterator)
        T = int(T_str)
    except StopIteration:
        return

    for _ in range(T):
        try:
            # Based on PDF:
            # Line 1: k
            # Line 2: n
            # Line 3: n integers (prices)
            
            k = int(next(iterator))
            n = int(next(iterator))
            prices = [int(next(iterator)) for _ in range(n)]
            
            # Optimization: If k >= n/2, we can capture every upward slope.
            if k >= n // 2:
                print(solve_greedy(n, prices))
            else:
                print(solve_dp(n, k, prices))
            
        except StopIteration:
            break

if __name__ == "__main__":
    solve()