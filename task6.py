# 6. Write a program to create a function show_employee() using the following conditions.
# (Напишите программу для создания функции, show_employee()используя следующие условия)

# It should accept the employee’s name and salary and display both.
# (Он должен принимать имя и зарплату сотрудника и отображать и то, и другое.)
# If the salary is missing in the function call then assign default value 9000 to salary.
# (Если в вызове функции отсутствует зарплата, присвойте зарплате значение по умолчанию 9000.)
# For example:
#     showEmployee("Ben", 12000)
#     showEmployee("Jessa")
# Output:
#     Имя: Бен Зарплата: 12000
#     Имя: Джесса Зарплата: 9000

def showEmployee(name, salary = 9000, dict_name = {}, list = []):
	dict_name[name] = salary
	#list.append(dict_name)
	#for i in list:
	for k, v in dict_name.items():
		print(f"Name: {k} Salary: {v}")

showEmployee("Ben", 12000)