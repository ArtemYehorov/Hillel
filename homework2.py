userinput = int(input('Введите целое 5-ти значное число: '))

a = userinput // 10000
b = userinput // 1000 % 10
c = userinput // 100 % 10
d = userinput // 10 % 10
f = userinput % 10

print((10000 * f) + (1000 * d) + (100 * c) + (10 * b) + a)