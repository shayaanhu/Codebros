# No 0 in s --- Print(0)
# IF len(s) > 5 and 0/1 both present --- Print(2)
# else 1

for _ in range(int(input())):
    # n = int(input())
    s = input().strip()
    
    if '0' not in s:
        print(0)
    # elif len(s) >= 5 and ('0' in s or '1' in s):
    # elif s[0] == '0' and s[-1] == '0' and s[1:-1].count('1') > 0:
    #     print(2) 
    # elif s.count('0') >= 2 and s.count('1') >= 1 and s.find('01') != len(s) - 1 and s.find('10') != 0:
    #     print(2)

    else:
        x = s.rfind('0')
        for i in range(len(s) - 2):
            if s[i] == '0' and s[i+1] == '1' and i != x:
                print(2)
                break
        else:
            print(1)

        # print(1)
    # print(s.find('01'), s.find('10'))

# How do I check if a string has consequent 0s? "...01...10..."