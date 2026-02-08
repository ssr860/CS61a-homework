def double_eights(n: int) -> bool:
    """Returns whether or not n has two digits in row that
    are the number 8.

    >>> double_eights(1288)
    True
    >>> double_eights(880)
    True
    >>> double_eights(538835)
    True
    >>> double_eights(284682)
    False
    >>> double_eights(588138)
    True
    >>> double_eights(78)
    False
    >>> # ban iteration, in operator and str function 
    >>> from construct_check import check
    >>> check(SOURCE_FILE, 'double_eights', ['While', 'For', 'In', 'Str'])
    True
    """
    "*** YOUR CODE HERE ***"
    if n<10:
        return False
    elif n%10==8 and (n//10)%10==8:
        return True
    else:
        return double_eights(n//10)
def main():
    result=double_eights(8800)
if __name__ =="__main__":
    main()