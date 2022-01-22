cipher = "CFb5cp0rm1gK{1r4nT_m4}6"
c = list(cipher)
for i in range(len(cipher)-1, -1, -1):
    for j in range(len(cipher) -2, i-1, -1):
        c[j], c[j+1] = c[j+1], c[j]
print("".join(c))