def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    "*** YOUR CODE HERE ***"
    if k != 0:
        tmp = n - k + 1
        for i in range(n - k + 1 , n):
            tmp, i = tmp * (i + 1), i + 1
    else: tmp = 1
    return tmp

def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    "*** YOUR CODE HERE ***"
    y = str(y)
    tmp = 0
    for i in range(len(y)):
        tmp = tmp + int(y[i]) 
        i = i + 1
    return tmp



def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"
    n = str(n)
    if len(n) == 1:
        return False
    else: 
        for i in range(len(n)):
            if i + 1 < len(n):
                if n[i] == n[i+1] and n[i] == '8': 
                    return True
            i = i + 1 
        return False


