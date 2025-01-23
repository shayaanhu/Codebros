# t = int(input())

# final = []
# for _ in range(t):
# 	n = int(input())
# 	a = input()
# 	b = input()
# 	c = input()
# 	t = ""
#     found = False
    
# 	if (a == c or b == c):
# 		final.append("NO")
# 		continue
# 	for i, j, k in zip(a, b, c):
# 		if (i == j or i == k):
# 			final.append("NO")
#             found = True
# 			break
# 	if found == False:
# 	    final.append("YES")
 
# for i in final:
#     print(i)
 

# # a b c
# # C
# # YES

t = int(input())

final = []
for _ in range(t):
	n = int(input())
	a = input()
	b = input()
	c = input()
	t = ""
	gg = False
 
	# if (a == c or b == c):
    # print("NO")

	for i, j, k in zip(a, b, c):
		if (i != k and j != k):
			gg = True
			break
   	
	if (gg):
		final.append("YES")
	else:
		final.append("NO")
  
for i in final:
    print(i)

# a b c
# C
# YES