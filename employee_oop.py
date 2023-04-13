class Employee:
    def __init__(self, name, dob, username, password, role, coesalary, worktime, bonus, salary):
        self.__name = name
        self.__dob = dob
        self.__username = username
        self.__password = password
        self.__role = role
        self.__coesalary = coesalary
        self.__worktime = worktime
        self.__bonus = bonus
        self.__salary = salary

    def set_salary(self, salary):
        self.__salary = salary
