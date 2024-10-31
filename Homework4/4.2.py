my_list = [0, 1, 7, 2, 4, 8]
if len(my_list) != 0:
    print(sum(my_list[0::2])*my_list[-1])
else:
    print(sum(my_list))