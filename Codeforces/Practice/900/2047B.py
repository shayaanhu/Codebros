t = int(input()) 
final = []

for _ in range(t):
    n = int(input())  
    s = list(input())  
    
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    
    max_freq_char = max(freq, key=freq.get)
    min_freq_char = min(freq, key=freq.get)
    
    if freq[max_freq_char] == freq[min_freq_char]:
        for i in range(n):
            if s[i] != s[0]:  
                s[i] = s[0]
                break
    else:
        for i in range(n):
            if s[i] == min_freq_char:
                s[i] = max_freq_char
                break
    
    final.append(''.join(s))

for result in final:
    print(result)

    

