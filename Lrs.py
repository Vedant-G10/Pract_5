def LRS(a, b):
   
    n = len(a)
    m = len(b)
    c = [[0] * (m + 1) for _ in range(n + 1)]

    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i - 1] == b[j - 1] and i != j:
                c[i][j] = 1 + c[i - 1][j - 1]  
            else:
                c[i][j] = max(c[i - 1][j], c[i][j - 1])  

    
    return c[n][m]

a = "AABEBCDD"
b = "AABEBCDD"
result = LRS(a, b)
print("Length of Longest Repeating Subsequence is:", result)
