# 7. Return a new set of identical items from two sets.
# (Верните новый набор одинаковых предметов из двух наборов.)
# Given:
#     set1 = {10, 20, 30, 40, 50}
#     set2 = {30, 40, 50, 60, 70}
# Expected output:
#     {40, 50, 30}

def set_identical(set1, set2, set3 = set()):
	for i in set1:
		if i in set2:
			set3.add(i)
	return set3

a = input().split()
b = input().split()
print(set_identical(a, b))