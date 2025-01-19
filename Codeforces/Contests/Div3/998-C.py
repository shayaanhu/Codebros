t = int(input())
final = []

for _ in range(t):
    temp = list(map(int, input().split()))
    n, k = temp[0], temp[1]

    nums = sorted(list(map(int, input().split())))
    score = 0

    left, right = 0, n - 1

    # print(nums)
    while left < right:
        if nums[left] + nums[right] == k:
            score += 1
            nums[left], nums[right] = 0.25, 0.25
            left += 1
            right -= 1
        elif nums[left] + nums[right] < k:
            left += 1
        else:
            right -= 1

    # for i in range(len(nums)):
    #     for j in range(len(nums)):
    #         if i != j and nums[i] + nums[j] == k:
    #             # print(i, j, nums)
    #             score += 1
    #             nums[i], nums[j] = 0.25, 0.25

    final.append(score)

for i in final:
    print(i)

