def is_even(digit):
    return (digit & 1) == 0

assert is_even(2494563894038**2) == True, 'Test1'
assert is_even(1056897**2) == False, 'Test2'
assert is_even(24945638940387**3) == False, 'Test3'
assert is_even(2) == True, 'Test4'
assert is_even(5) == False, 'Test5'
assert is_even(0) == True, 'Test6'
print('OK')