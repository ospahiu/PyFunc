"""
GPL open license.
@author ospahiu
"""


def split_list_on_condition(sequence, cond):
    unwanted, wanted = [], []
    for item in sequence:
        (unwanted, wanted)[cond(item)].append(item)
    return unwanted, wanted


def bucket_on_conditions(sequence, conditions):
    buckets = tuple([] for _ in range(len(conditions)))
    for item in sequence:
        for index, condition in enumerate(conditions):
            if condition(item):
                buckets[index].append(item)
    return buckets

def zip_with(function, sequence_one, sequence_two):
    for first, second in zip(sequence_one, sequence_two):
        yield function(first, second)

print zip_with(lambda x, y: x + y, [1, 2, 3], [1, 2, 3])