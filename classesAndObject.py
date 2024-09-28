class employee:
    def __init__(self, id = None, name = None, salary = None):
        self.id = id
        self.name = name
        self.salary = salary

    # this is are the setters 

    def setId(self, id):
        self.id = id

    def setName(self, name):
        self.name = name

    def setSalary(self, salary):
        self.salary = salary
    
    # this is are the getters 

    def getId(self):
        return self.id
    
    def getName(self):
        return self.name
    
    def getSalary(self):
        return self.salary
    

emp1 = employee(1, "umesh", 150000000);
print(emp1.getId(), emp1.getName(), emp1.getSalary())