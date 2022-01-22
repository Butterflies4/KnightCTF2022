a = 21525625
b = 30135875
def gcd(a,b):
    if a == b: return a
    elif a<b: return gcd(a, b-a)
    else: return gcd(a-b,b)
print(gcd(a,b))
print(20*1234)