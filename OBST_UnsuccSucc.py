# daa-pract-6

def initialize_matrices(n, q):
  
    e = [[0] * (n + 1) for _ in range(n + 1)]
    w = [[0] * (n + 1) for _ in range(n + 1)]

  
    for i in range(n + 1):
        e[i][i] = q[i]
        w[i][i] = q[i]

    print("Step 1: Initialization")
    print("Matrix e after initialization:")
    print_matrix(e, n)
    print("Matrix w after initialization:")
    print_matrix(w, n)
    print("-" * 40)

    return e, w

def calculate_costs(e, w, p, q, n):

    for length in range(1, n + 1):
        for i in range(n - length + 1):
            j = i + length
            e[i][j] = float('inf')
            w[i][j] = w[i][j - 1] + p[j - 1] + q[j]

        
            for r in range(i + 1, j + 1):
                cost = e[i][r - 1] + e[r][j] + w[i][j]
                if cost < e[i][j]:
                    e[i][j] = cost

        print(f"Step 2: Costs and weights for subtrees of length {length}")
        print("Matrix e:")
        print_matrix(e, n)
        print("Matrix w:")
        print_matrix(w, n)
        print("-" * 40)

def print_matrix(matrix, n):

    for i in range(n + 1):
        row = []
        for j in range(n + 1):
            if j >= i:
                row.append(f"{matrix[i][j]:.4f}")
            else:
                row.append("    - ")
        print(" ".join(row))
    print()

def optimal_bst(keys, p, q, n):
  
    e, w = initialize_matrices(n, q)
    calculate_costs(e, w, p, q, n)
    

    return e[0][n]

n = 4
keys = [10, 20, 30, 40]
p = [0.1, 0.2, 0.4, 0.3]
q = [0.05, 0.1, 0.05, 0.05, 0.1]


min_cost = optimal_bst(keys, p, q, n)
print(f"Minimum expected search cost: {min_cost:.4f}")
