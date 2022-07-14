
import datetime

class Employee:

    def __init__(self,name,age,salary,employment_year) :
        self.name = name
        self.age = age
        self.salary = salary
        self.employment_year = employment_year

    def get_working_years(self):
        year = datetime.date.today() - self.employment_year
        return year
    

     
   
employeeList = []
employeeList.append(Employee("heba",28,100,4))
employeeList.append(Employee("reem",30,1000,19))
employeeList.append(Employee("farah",27,1500,6))




class Manager(Employee):
    def __init__(self, name, age, salary, employment_year,bonus_percentage):
        super().__init__(name, age, salary, employment_year)
        self.bonus_percentage = bonus_percentage
    
    def get_bonus(self):
        result = self.bonus_percentage * self.salary
        return result
        

ManagerList = []
ManagerList.append(Manager("Galya",27,2000,16,90))
ManagerList.append(Manager("ahmad",30,3000,20,40))
ManagerList.append(Manager("dalal",27,1500,6,60))

  


# employee1 = Employee("heba","28","1000",5)
# employee2 = Employee("farah","28","1000",4)
# print(employee1.name)

# manager1= Manager("ghalya","28","1000",4,90)
# manager2= Manager("reem","28","1000",4,90)
# print(manager1.bonus_percentage)






def main():
    ...
	# main code here
print("Welcome to HR Pro 2019")
print("Options:")
x = int(input(print("1. Show Employees\n2. Show Managers\n3. Add an Employee\n4. Add A manager\n5. Exit")))

if (x==1):
    for x in employeeList:
        print('\nName : {}\nAge : {}\nSalary : {} \nEmployment year: {}\n\n'.format(x.name,x.age,x.salary,x.employment_year))

elif (x==2):
    for x in ManagerList:
        print('\nName : {}\nAge : {}\nSalary : {} \nEmployment year: {}\nBouns percentage: {}\n\n'.format(x.name,x.age,x.salary,x.employment_year,x.bonus_percentage))








if __name__ == '__main__':
	main()
