"""
Write a function that takes a list and returns a new list that contains
all the elements of the first list without duplicates.
"""


def deduplicate_list(items):
    return list(set(items))


def deduplicate_and_keep_order(items):
    deduplicated_items = []
    for item in items:
        if item not in deduplicated_items:
            deduplicated_items.append(item)
    return deduplicated_items


example = ["a", "b", "c", "a", "b"]
print("Original list: %s" % example)
print(deduplicate_list(["a", "b", "c", "a", "b"]))
print(deduplicate_and_keep_order(["a", "b", "c", "a", "b"]))
