t = int(input())
for _ in range(t):
	s = input()
	n = len(s)
	ones = []

	for i in range(n):
		if s[i] == '1':
			ones.append(i)

	if not ones:
		print(0)
		continue

	count = 0
	while ones:
		count += 1
		new_ones = []
		last_flipped = -1
		
		for i in ones:
			if last_flipped == -1 or (s[i] != s[last_flipped] and i!=last_flipped):
				last_flipped = i
			else:
				new_ones.append(i)
		ones = new_ones

	print(count)
