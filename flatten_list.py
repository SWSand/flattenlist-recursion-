def flatten_list(lst, i=0, result = []):
    result = []

    for item in lst:
        if isinstance(item, int):
            result.append(item)
        elif isinstance(item,list):
            # print(result)
            result.extend(flatten_list(item))
    return result


tst1 = [1, 2, [3], [4,5]]
# output = [1, 2, 3, 4, 5]
tst2 = [1, [2], [3, [4, 5, [6]]], 7]
# output = [1, 2, 3, 4, 5, 6, 7]

print(flatten_list(tst1))
print(flatten_list(tst2))



