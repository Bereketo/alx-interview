#!/usr/bin/python3
"""Minumum Operations """


def minOperations(n):
    """Arguments:
            n: number of times character have to be repeated
       Returns:
            operation: int -> minimum operation
                        to get a character repeated n times
    """
    txt = ['H']
    cpAmount = 1
    op = 0
    while len(txt) < n:
        if len(txt) == 1:
            op += 2
            txt.extend(txt)
        elif n % len(txt) == 0:
            op += 2
            cpAmount = len(txt)
            txt.extend(txt)
        else:
            op += 1
            for i in range(cpAmount):
                txt.append(txt[i])
    if len(txt) > n:
        return 0
    return op
