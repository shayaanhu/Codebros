# 0 ---- 9999....9999

# POSSIBLE STEPS
# Decrement by 1
# Swap any two digits

# Add the non-zero digits of the number together
# Count the non-zero digits of the number
# If the right-most digit is non-zero, then add count - 1 to the result else add count to the result


def solve(n):
    n = str(n)
    result = 0
    count = 0

    for i in range(len(n) - 1, -1, -1):
        if n[i] != '0':
            count += 1
            result += int(n[i])
    
    result += count - 1 if n[-1] != '0' else count

    return result if result > 0 else 0


for _ in range(int(input())):
    num = int(input())
    n = int(input())
    print(solve(n))