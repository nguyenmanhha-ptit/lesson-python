import time

n = input("nhap :").split()
t = tuple(n)
def count_in_tuple(t, x):
    return t.count(x)
t1 = time.time()
t2 = time.get_clock_info()

for x in set(t):
    print(f"Giá trị {x} xuất hiện {count_in_tuple(t, x)} lần")


t2 = time.time()
print('Elapsed time: {} seconds'.format((t2 - t1)))