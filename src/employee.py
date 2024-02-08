class Employee:

    def __init__(self, name, age, experience):
        self.name = name
        self.age = age
        self.experience = experience

    def info(self):
        print(f"Name: {self.name}; Age: {self.age}")

    def calculate_salary(self):
        salary = 1000*self.age
        return salary
    
