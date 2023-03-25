class Employee:
    def __init__(self, first_name, second_name, base_salary, experience):
        self.first_name = first_name
        self.second_name = second_name
        self.base_salary = base_salary
        self.experience = experience
        self.countedSalary = base_salary

        if self.experience > 5:
            self.countedSalary = 1.2 * self.countedSalary + 500
        elif self.experience > 2:
            self.countedSalary += 200


class Developer(Employee):
    def __init__(self, first_name, second_name, base_salary, experience):
        super().__init__(first_name, second_name, base_salary, experience)


class Designer(Employee):
    def __init__(self, first_name, second_name, base_salary, experience, coefficient):
        super().__init__(first_name, second_name, base_salary, experience)
        self.coefficient = coefficient
        self.countedSalary = int(self.coefficient * self.countedSalary)


class Manager(Employee):
    def __init__(self, first_name, second_name, base_salary, experience, team):
        super().__init__(first_name, second_name, base_salary, experience)
        self.team = team

        if len(self.team) > 10:
            self.countedSalary += 300
        elif len(self.team) > 5:
            self.countedSalary += 200

        developers = len([employee for employee in self.team if isinstance(employee, Developer)])
        if developers > (len(self.team) / 2):
            self.countedSalary = int(1.1 * self.countedSalary)


class Department:
    def __init__(self, managers):
        self.managers = managers

    def give_salary(self):
        output = ""
        for manager in self.managers:
            output += f"{manager.first_name} {manager.second_name} отримав {manager.countedSalary} шекєлей\n"
            for employee in manager.team:
                output += f"{employee.first_name} {employee.second_name} отримав {employee.countedSalary} шекєлей\n"
        print(output)


# Перший менеджер та його команда
Viktor = Developer("Viktor", "Katerynych", 550, 1)
John = Developer("John ", "Wilson", 1300, 1.5)
Dave = Developer("Dave", "Martinez", 2200, 2.5)
Stella = Designer("Stella", "Graves", 550, 1, 0.6)
Steve = Manager("Steve", "Holland", 5000, 4.5, [Viktor, John, Dave, Stella])

# Другий менеджер та його команда
Emily = Developer("Emily", "Garcia", 4000, 3.5)
Liam = Developer("Liam", "Patel", 4200, 4.5)
Olivia = Designer("Olivia", "Kim", 2500, 3, 0.8)
Ethan = Designer("Ethan", "Nguyen", 700, 1, 0.7)
Mia = Designer("Mia", "Singh", 5500, 8.5, 1)
William = Designer("William", "Chen", 4000, 6, 0.9)
Sophia = Manager("Sophia", "Rodriguez", 3700, 4, [Emily, Liam, Olivia, Ethan, Mia, William])

dep = Department([Steve, Sophia])
dep.give_salary()
 
