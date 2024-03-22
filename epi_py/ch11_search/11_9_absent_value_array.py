import itertools
from typing import Iterator


def find_missing_element(stream: Iterator[int]) -> int:

    num_bucket = 1 << 16
    counter = [0] * num_bucket
    stream, stream_copy = itertools.tee(stream)
    for x in stream:
        upper_part_x = x >> 16
        counter[upper_part_x] += 1

    # Look for a bucket that contains less than (1 << 16) elements.
    bucket_capacity = 1 << 16
    candidate_bucket = next(i for i, c in enumerate(counter)
                            if c < bucket_capacity)

    # Finds all IP addresses in the stream whose first 16 bits are equal to
    # candidate_bucket.
    candidates = [0] * bucket_capacity
    for x in stream_copy:
        upper_part_x = x >> 16
        if candidate_bucket == upper_part_x:
            # Records the presence of 16 LSB of x.
            lower_part_x = ((1 << 16) - 1) & x
            candidates[lower_part_x] = 1

    # At least one of the LSB combinations is absent, find it.
    for i, v in enumerate(candidates):
        if v == 0:
            return (candidate_bucket << 16) | i

    raise ValueError('no missing element')


def find_missing_element_wrapper(stream):
    try:
        res = find_missing_element(iter(stream))
        if res in stream:
            raise Exception('{} appears in stream'.format(res))
    except ValueError:
        raise Exception('Unexpected no missing element exception')



