def MaxCrossingSum(A, low, mid, high):
left_sum = float(&#39;-inf&#39;) total = 0 for i in
range(mid, low - 1, -1): total += A[i] if
total &gt; left_sum:
left_sum = total
right_sum = float(&#39;-inf&#39;) total = 0
for j in range(mid + 1, high + 1):
total += A[j] if total
&gt; right_sum:
right_sum = total
return left_sum + right_sum
def MaxSubarraySum(A, low, high):
if low == high:
return A[low]
mid = (low + high) // 2 left_sum =
MaxSubarraySum(A, low, mid) right_sum =
MaxSubarraySum(A, mid + 1, high) cross_sum =
MaxCrossingSum(A, low, mid, high) return
max(left_sum, right_sum, cross_sum)
def max_subarray_sum_with_constraint(resources, constraint):
n = len(resources)
max_sum = 0
current_sum = 0
start = 0
best_subarray = None
for end in range(n):
current_sum += resources[end] while
current_sum &gt; constraint and start &lt;= end:
current_sum -= resources[start]
start += 1
if current_sum &lt;= constraint and current_sum &gt; max_sum:
max_sum = current_sum best_subarray =
resources[start:end+1]
return max_sum, best_subarray
def run_tests():

test_cases = [
([2, 1, 3, 4], 5, &quot;Test 1: Basic small array&quot;),
([2, 2, 2, 2], 4, &quot;Test 2: Exact match to constraint&quot;),
([1, 5, 2, 3], 5, &quot;Test 3: Single element equals constraint&quot;),
([6, 7, 8], 5, &quot;Test 4: No valid subarray&quot;),
([1, 2, 3, 2, 1], 5, &quot;Test 5: Multiple optimal subarrays&quot;),
([1, 1, 1, 1, 1], 4, &quot;Test 6: Large window valid&quot;),
([4, 2, 3, 1], 5, &quot;Test 7: Sliding window shrink needed&quot;),
([], 10, &quot;Test 8: Empty array&quot;),
([1, 2, 3], 0, &quot;Test 9: Constraint = 0&quot;),
(list(range(1, 100001)), 10**9, &quot;Test 10: Very large input&quot;),
]
for resources, constraint, description in test_cases:
print(description)
max_sum, subarray = max_subarray_sum_with_constraint(resources, constraint)
print(f&quot;Constraint: {constraint}&quot;) print(f&quot;Max Sum ≤ Constraint: {max_sum}&quot;)
print(f&quot;Subarray: {subarray if subarray else &#39;No valid subarray&#39;}\n&quot;)
run_tests()
