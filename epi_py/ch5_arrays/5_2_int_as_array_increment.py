"""
TRICK: 
STEP 1: NAIVELY +=1 TO THE LAST ELEMENT.
STEP 2: CHECK FOR 10 ALL THE WAY FROM END TO INDEX 1 (REVERSED OBVIOUSLY)
STEP 3: FINAL CHECK IF INDEX 0 == 10
"""

from typing import List

from test_framework import generic_test


def plus_one(A: List[int]) -> List[int]:

    A[-1] += 1
    for i in reversed(range(1, len(A))):
        if A[i] != 10:
            break
        A[i] = 0
        A[i - 1] += 1
    else:
        if A[0] == 10:
            # There is a carry-out, so we need one more digit to store the result.
            # A slick way to do this is to append a 0 at the end of the array,
            # and update the first entry to 1.
            A[0] = 1
            A.append(0)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_increment.py',
                                       'int_as_array_increment.tsv', plus_one))
