a = "AGCCCTAAGGGCTACCTAGCTT"
b = "GACAGCCTACAAGCGTTAGCTTG"
c = {}
m = len(a)
n = len(b)
e = ""

for i in range(m + 1):
    for j in range(n + 1):
        if i == 0 or j == 0:
            c[(i, j)] = (0, "h")  
        else:
            if a[i - 1] != b[j - 1]:  
                top = c[(i - 1, j)][0]
                left = c[(i, j - 1)][0]
                d = max(top, left)
                if top >= left:
                    e = "u"
                else:
                    e = "s"  
                c[(i, j)] = (d, e)
            else:
                f = c[(i - 1, j - 1)][0] + 1
                g = "d"  
                c[(i, j)] = (f, g)


for i in range(m + 1):
    row = []
    for j in range(n + 1):
        row.append(f"{c[(i, j)][0]}/{c[(i, j)][1]}")
    print(" ".join(row))


print(f"LCS Length is: {c[(m, n)][0]}")
