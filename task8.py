# 8. Write a recursive function is_polindrom(str) to check if a given string is a palindrome.
# (Напишите рекурсивную функцию, проверяющую, является ли данная строка палиндромом.)
# Input:                          Input:
#     banana                          abccba
# Output:                         Output:
#     False                           True

def poli(a):
	if len(a) <= 1:
		return True
	if a[0] != a[-1]:
		return False
	return poli(a[1:-1])