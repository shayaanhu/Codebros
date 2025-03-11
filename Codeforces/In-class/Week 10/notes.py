"""
Ways to calculate binomial coefficient nCk:

1. Pascal's triangle:
/** @return nCk mod p using naive recursion */
int binomial(int n, int k, int p) {
	if (k == 0 || k == n) { return 1; }
	return (binomial(n - 1, k - 1, p) + binomial(n - 1, k, p)) % p;
}

2. n! / (n - k)! * k!

3. math.comb(n, k)

"""

# Question = Binomial Coefficients (CSES)

# Attempt 1 (TLE)
# use math.comb(a, b) % m

# Attempt 2
# Instead, cache/precompute the factorials (and mod them)
# get factorial for 1 to n
# start with 0! = 1
# then 1! = 1
# 2! = 1 * 2
# 3! = 1 * 2 * 3
# since we want inverse, i.e. (n!)^-1, we do 1/ 1 * 2 * 3
# we want inverse because dividing by (n - 1)! and k!
# so we multiply by inverse of the next number
# and % it