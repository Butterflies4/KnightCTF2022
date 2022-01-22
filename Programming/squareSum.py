from math import trunc,sqrt
for x in range(25000):
    tmp = 25000-x*x
    if trunc(sqrt(tmp))*trunc(sqrt(tmp))==tmp:
        print(x,sqrt(tmp))