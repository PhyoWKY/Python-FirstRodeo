employee_file = open("employees.txt", "a")
employee_file.write("\nMichael = Accountant")
employee_file.close()

#employee_file = open("employees.txt", "w")
#employee_file.write("\nMichael = Accountant")
#This will overwrite the file

employee_file  = open("employees1.txt", "w")
employee_file.write("\nJack = Accountant")
employee_file.close()
#Making a new file

employee_file = open("index.html", "w")
employee_file.write("<p>Hello World!</p>")
employee_file.close()
#Create a new HTML file