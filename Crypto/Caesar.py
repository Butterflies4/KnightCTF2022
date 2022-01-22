text="XPGS{DE_pbqr_tbg_ribyirq_sebz_fgngvp_gb_qlanzvp}"
l_c = ''.join(chr(c) for c in range (97,123)) 
u_c = ''.join(chr(c) for c in range (65,91)) 
l_e = l_c[13:] + l_c[:13]
u_e = u_c[13:] + u_c[:13]
print(l_e)
so = ""
for c in text:
    if c in l_c:
        so = so + l_e[l_c.find(c)]
    elif c in u_c:
        so = so + u_e[u_c.find(c)]
    else:
        so = so + c
print(so)