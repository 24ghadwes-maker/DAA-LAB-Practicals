def optimalSearchTree(keys, freq, n):
    cost = [[0 for x in range(n)] for y in range(n)]

    for i in range(n):
        cost[i][i] = freq[i]

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            cost[i][j] = float('inf')

            for r in range(i, j + 1):
                left_cost = 0
                if r > i:
                    left_cost = cost[i][r - 1]

                right_cost = 0
                if r < j:
                    right_cost = cost[r + 1][j]

                sum_freq = sum(freq[i : j + 1])
                current_cost = left_cost + right_cost + sum_freq

                if current_cost < cost[i][j]:
                    cost[i][j] = current_cost

    return cost[0][n - 1]

keys1 = [10, 12]
freq1 = [34, 50]
n1 = len(keys1)
print(f"Input: keys = {keys1}, freq = {freq1}, n = {n1}")
print(f"Output: {optimalSearchTree(keys1, freq1, n1)}")

keys2 = [10, 12, 20]
freq2 = [34, 8, 50]
n2 = len(keys2)
print(f"\nInput: keys = {keys2}, freq = {freq2}, n = {n2}")
print(f"Output: {optimalSearchTree(keys2, freq2, n2)}")
