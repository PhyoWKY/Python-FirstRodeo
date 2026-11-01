employee_file = open("employees.txt","r") # also w, a, r+

print(employee_file.readable())

#print(employee_file.read())

#print(employee_file.readlines())
#print(employee_file.readlines()[1])

#print(employee_file.readline())
#print(employee_file.readline())

for employee in employee_file.readlines():
    print(employee)

employee_file.close()

