# DAA-LAB-Practicals
X="AGCCCTAAGGGCTACCTAGCTT"
Y= "GACAGCCTACAAGCGTTAGCTTG"
m = len(X)
n = len(Y)
c = []
b = []
for i in range(m+1):
c.append([0] * (n+1))
b.append(['-'] * (n+1))
def print_matrices():
print("\nMatrix c (lengths) and directions:")
print(" ", end="")
for ch in Y:
print(f" {ch} ", end="")
print()
for i in range(m+1):

if i == 0:
print(" ", end=" ")
else:
print(f"{X[i-1]} ", end="")
for j in range(n+1):
if i == 0 or j == 0:
print(f" {c[i][j]:2} ", end="")
else:
print(f"{c[i][j]}{b[i][j]} ", end="")

print()

print("Initial matrices:")
print_matrices()
for i in range(1, m+1):
for j in range(1, n+1):
if X[i-1] == Y[j-1]:
c[i][j] = c[i-1][j-1] + 1
b[i][j] = '↖'
elif c[i-1][j] >= c[i][j-1]:
c[i][j] = c[i-1][j]
b[i][j] = '↑'
else:
c[i][j] = c[i][j-1]
b[i][j] = '←'

print(f"\nAfter updating c[{i}][{j}] (X[{i-1}]='{X[i-1]}',

Y[{j-1}]='{Y[j-1]}'):")
print_matrices()

print(f"\nLength of LCS = {c[m][n]}")
