
import datetime

class Employee:

    def __init__(self,name,age,salary,employment_year) :
        self.name = name
        self.age = age
        self.salary = salary
        self.employment_year = employment_year

    def get_working_years(self):
        year = int(datetime.date.today().year) - self.employment_year
        return year
    


     
   
employeeList = [Employee("heba",28,100,2020),Employee("reem",30,1000,2019),Employee("farah",27,1500,2018)]




class Manager(Employee):
    def __init__(self, name, age, salary, employment_year,bonus_percentage,):
        super().__init__(name, age, salary, employment_year)
        self.bonus_percentage = bonus_percentage
    
    def get_working_years(self):
        manager_year =int(datetime.date.today().year)  - self.employment_year
        return manager_year 

    def get_bonus(self):
        result = self.bonus_percentage * self.salary
        return result
        

ManagerList = [Manager("Galya",27,2000,16,90),Manager("ahmad",30,3000,20,40),Manager("dalal",27,1500,6,60)]

  








def main():
    ...
	# main code here

print("Welcome to HR Pro 2019")
print("Options:")

x=0
while (x!=5):
    print("1. Show Employees\n2. Show Managers\n3. Add an Employee\n4. Add A manager\n5. Exit\n")
    
    x = int(input("what would you like to do:  "))
    print("-------------------------------\n\n")
   
   

    if (x==1):
     for x in employeeList:
        print('\nName : {}\nAge : {}\nSalary : {} \nEmployment year: {}\n\n'.format(x.name,x.age,x.salary,x.employment_year))
        print(Employee.get_working_years())

    elif (x==2):
        for x in ManagerList:
            print('\nName : {}\nAge : {}\nSalary : {} \nEmployment year: {}\nBouns percentage: {}\n\n'.format(x.name,x.age,x.salary,x.employment_year,x.bonus_percentage))
   



   
# add Employee 
    elif (x==3):
        name1=input("Name:  ")
        age1=int(input("Age:  "))
        salary1=int(input("Salary: "))
        employement_year1=int(input("Employment Year: "))
        print("Employee added succesfully")
        employeeList.append(Employee(name1,age1,salary1,employement_year1))
        


# add Manager 


    elif (x==4):
        name1=input("Name:  ")
        age1=int(input("Age:  "))
        salary1=int(input("Salary: "))
        employement_year1=int(input("Employment Year: "))
        bonus1=float(input("Bonus Percentage: "))
        
        print("Manager added succesfully")
        ManagerList.append(Manager(name1,age1,salary1,employement_year1,bonus1))
       # print(Manager.get_bonus(bonus1))


        
    else:
        print("Thank you !")






if __name__ == '__main__':
	main()
