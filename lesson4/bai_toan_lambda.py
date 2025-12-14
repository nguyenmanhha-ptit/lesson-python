import numpy as np

# Cac vector cho truoc
u = np.array([2, 3, 5])
v = np.array([3, 7, 8])
w = np.array([1, -6, 1])
x = np.array([7, -2, None])  # λ chua biet

# De x la to hop tuyen tinh cua u, v, w: x = a*u + b*v + c*w
# Ta co he phuong trinh:
# 2a + 3b + c = 7
# 3a + 7b - 6c = -2
# 5a + 8b + c = λ

# Giai he 2 phuong trinh dau de tim a, b, c
# He phuong trinh:
A = np.array([
    [2, 3, 1],   # 2a + 3b + c = 7
    [3, 7, -6],  # 3a + 7b - 6c = -2
])
b = np.array([7, -2])

# Giai he phuong trinh
# Co 2 phuong trinh, 3 an so -> co the bieu dien 1 an theo 2 an con lai
# Hoac kiem tra tung gia tri λ

print("=== Giai bai toan tim λ ===\n")
print("Cho:")
print(f"x = (7, -2, λ)")
print(f"u = {u}")
print(f"v = {v}")
print(f"w = {w}\n")

print("De x la to hop tuyen tinh cua u, v, w:")
print("x = a*u + b*v + c*w\n")

print("He phuong trinh:")
print("2a + 3b + c = 7")
print("3a + 7b - 6c = -2")
print("5a + 8b + c = λ\n")

# Kiem tra tung gia tri λ
lambda_values = [10, 12, -11, 11]

print("=== Kiem tra cac gia tri λ ===\n")

for lam in lambda_values:
    # Tao he phuong trinh day du
    A_full = np.array([
        [2, 3, 1],
        [3, 7, -6],
        [5, 8, 1]
    ])
    b_full = np.array([7, -2, lam])
    
    try:
        # Giai he phuong trinh
        solution = np.linalg.solve(A_full, b_full)
        a, b, c = solution
        
        # Kiem tra lai
        x_check = a*u + b*v + c*w
        x_expected = np.array([7, -2, lam])
        
        if np.allclose(x_check, x_expected):
            print(f"✓ λ = {lam}: DUNG!")
            print(f"  a = {a:.2f}, b = {b:.2f}, c = {c:.2f}")
            print(f"  Kiem tra: {a}*u + {b}*v + {c}*w = {x_check}")
            print(f"  Mong doi: x = {x_expected}\n")
        else:
            print(f"✗ λ = {lam}: SAI")
            print(f"  {x_check} ≠ {x_expected}\n")
    except np.linalg.LinAlgError:
        print(f"✗ λ = {lam}: He phuong trinh vo nghiem hoac vo so nghiem\n")

# Cach 2: Giai bang cach rut gon
print("\n=== Cach giai chi tiet ===\n")
print("Tu 2 phuong trinh dau:")
print("2a + 3b + c = 7  =>  c = 7 - 2a - 3b")
print("3a + 7b - 6c = -2")
print("\nThe c vao phuong trinh 2:")
print("3a + 7b - 6(7 - 2a - 3b) = -2")
print("3a + 7b - 42 + 12a + 18b = -2")
print("15a + 25b = 40")
print("3a + 5b = 8  =>  a = (8 - 5b)/3\n")

# Thu b = 1
b_test = 1
a_test = (8 - 5*b_test) / 3
c_test = 7 - 2*a_test - 3*b_test
lambda_calc = 5*a_test + 8*b_test + c_test

print(f"Thu b = {b_test}:")
print(f"  a = {a_test:.2f}")
print(f"  c = {c_test:.2f}")
print(f"  λ = 5a + 8b + c = {lambda_calc:.2f}\n")

# Thu b = -1
b_test2 = -1
a_test2 = (8 - 5*b_test2) / 3
c_test2 = 7 - 2*a_test2 - 3*b_test2
lambda_calc2 = 5*a_test2 + 8*b_test2 + c_test2

print(f"Thu b = {b_test2}:")
print(f"  a = {a_test2:.2f}")
print(f"  c = {c_test2:.2f}")
print(f"  λ = 5a + 8b + c = {lambda_calc2:.2f}")

