# 2. Write a function to remove characters from a string starting from zero up to n and return a new string.
#     (Напишите функсию для удаления символов из строки, начиная с нуля и до, n и возврата новой строки.)
#     For example:
# Input                                   input
#     remove_chars("pynative", 4)             remove_chars("pynative", 2)
# Output                                  Output
#     tive                                    native

def remove_char(word, n, str = ""):
	for i in range(len(word)):
		if i >= n:
			str += word[i]
	return str