# 5. Find the sum of the series upto n terms(Найдите сумму ряда до n членов).
# For example:
#     n = 5
#     m = 2
# Output
#     2 + 22 + 222 + 2222 + 22222 = 24690

def sum_num(n, m, sum = 0):
	s = m
	for i in range(n):
		sum += int(m)
		m = m * 10 + s
	return sum

print(sum_num(5, 2))