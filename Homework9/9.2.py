def difference(*args):
    diff = 0
    if len(args) != 0:
        numbers = list(args)
        max_num = max(numbers)
        min_num = min(numbers)
        diff = max_num - min_num
    return round(diff,2)

assert difference(1, 2, 3) == 2, 'Test1'
assert difference(5, -5) == 10, 'Test2'
assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3'
assert difference() == 0, 'Test4'
print('OK')