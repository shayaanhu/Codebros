
import bisect

bro = []
# for i in range(int(1e9)):
#     # append if i is a square/cube
#     if int(i**0.5)**2 == i or int(i**(1/3))**3 == i:
#         bro.append(i)

for i in range(1, 1001):
    bro.append(i**3)

for j in range(1, 31623):
    bro.append(j**2)

bro = list(set(bro))
bro.sort()
bro_len = len(bro)

for _ in range(int(input())):
    n = int(input())
    # print(bro_len - bro.index(n) - 1)

    count = bisect.bisect_right(bro, n)
    print(count)
