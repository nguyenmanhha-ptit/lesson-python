
list=[1,2,3,4,5,6,7,8,9,10]
list1=set(list)
my_dict = {}
count={}
def count_in_tuple(list, item):
    return list.count(item)
for item in list1:
    my_dict[item] = count_in_tuple(list, item)
print(my_dict)