list = input(" nhap gia tri :").split()
def sum(list):
    sum = 0
    for i in list:
        sum += int(i)
    return sum
print(sum(list))