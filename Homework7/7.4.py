def common_elements():
    list1 = [x for x in range(0, 100, 3)]
    list2 = [x for x in range(0, 100, 5)]

    common = set(set(list1) & set(list2))
    return common

print(common_elements())