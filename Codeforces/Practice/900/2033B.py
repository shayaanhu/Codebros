t = int(input())

for _ in range(t):

	n = int(input())
	grid = [list(map(int, input().split())) for __ in range(n)]
	ans = 0

	# print("GRID:", grid)

	for i in range(n):
		t = i
		maxi = 0
		for j in range(n):
			if t >= n:
				break
			# print(t, j)
			if grid[t][j] < 0:
				maxi = max(maxi, -grid[t][j])
			t += 1
		ans += maxi

	for j in range(1, n):
		t = j
		maxi = 0
		for i in range(n):
			if t >= n:
				break
			if grid[i][t] < 0:
				maxi = max(maxi, -grid[i][t])
			t += 1
		ans += maxi

	print(ans)
