_list1 = [1,2,3,4,]

print(_list1)

if len(_list1) > 1:
    _list1.insert(0,_list1.pop(-1))
    #_list1.insert(0, _list1[-1]) Подскажите пожалуйста как будет правильнее
    #_list1.pop(-1)

print(_list1)

