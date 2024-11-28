def pow(x):
    return x ** 2

def some_gen(begin, end, func):
    count = 0
    while count < end:
        yield begin
        begin = func(begin)
        count += 1

from inspect import isgenerator

gen = some_gen(2, 6, pow)
gen2 = some_gen(3,5, pow)
assert isgenerator(gen) == True, 'Test1'
assert list(gen) == [2, 4, 16, 256, 65536, 4294967296], 'Test2'
assert list(gen2) == [3, 9, 81, 6561, 43046721], 'Test3'
print('OK')