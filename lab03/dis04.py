def paths(m,n):
    if m==1 or n==1:
        return 1
    else:
        return paths(m-1,n)+paths(m,n-1)
    
def max_products(s):
    if len(s)==0:
        return 1
    with_0=s[0]*max_products(s[2:])
    without_0=max_products(s[1:])
    if with_0>without_0:
        return with_0
    else:
        return without_0
    
def sum_fun(n,m):
    if n<0:
        return[]
    if n==0:
        sums_to_zero=[]
        return [sums_to_zero]
    result=[]
    for k in range(1,m+1):
        result=result+[[k]+rest for rest in sum_fun(n-k,m) if rest==[] or k!=rest[0]]
        return result