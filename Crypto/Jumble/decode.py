cipher = "0Un5Hfz02zQ=NtVB0=RZfMSX"
# cipher="gyngcroguntneuon"
c = list(cipher)
for i in range(len(cipher)-1, -1, -1):
    for j in range(len(cipher) -2, i-1, -1):
        c[j], c[j+1] = c[j+1], c[j]
print("".join(c))
# --> KCTF{y0u_g0t_m3}