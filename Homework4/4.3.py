import random
my_list = [random.randint(1,20) for i in range(random.randint(3,10))]
print(my_list)

small_list = [my_list[0], my_list[2], my_list[-2]]
print(small_list)