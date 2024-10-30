Father_list = [1,2,3,4,5,6]
Big_list = []
middle_of_list = len(Father_list) // 2 if len(Father_list) % 2 == 0 else (len(Father_list) // 2) + 1

child_list1 = Father_list[:middle_of_list]
child_list2 = Father_list[middle_of_list:]

Big_list.append(child_list1)
Big_list.append(child_list2)

print(Father_list)
print(Big_list)