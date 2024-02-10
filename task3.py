# 3. Return the count of a given substring from a string.
# (Возврат количества заданной подстроки из строки)
# Input
#     str_x = "Emma is good developer. Emma is a writer"
#     substring = "Emma"
# Output
#     2

def find_cnt(str_x, str_y, cnt = 0):
	for i in str_x:
		if i == str_y:
			cnt +=1
	return cnt

a = input().split()
b = input()
print(find_cnt(a, b))