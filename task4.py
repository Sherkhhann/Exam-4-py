# 4. Print the following pattern.(Распечатайте следующий шаблон.)
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
# 6 6 6 6
# 7 7 7
# 8 8
# 9

def pyramyd(a, t = 1):
	n = a // 2
	s = a
	for i in range(1, n+1):
		for j in range(i):
			print(t, end = " ")
		t += 1
		print()
	for k in range(n+1):
		for v in range(n+1):
			print(t, end=" ")
		print()
		t += 1
		n -= 1 
pyramyd(9)