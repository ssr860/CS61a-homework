def has_path(t,p):
    if p == label(t) and len(p)==1:
        return True
    elif label(t)!=p[0]:
        return False
    else:
        for b in branches(t):
            if has_path(b,p[1:]):
                return True
        return False
    

def find_path(t,x):
    if label(t)==x:
        return [x]
    elif label(t)!=x and branches(t):
        for b in branches(t):
            if find(b,x) is not None:
                return [label(t)]+find_path(b,x)
    return None