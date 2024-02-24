





class Employee(object):
    def __init__(self, firstname, lastname, salary = 0):
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary

    def __str__(self):
        return 'Full Name: ' + self.firstname + ' ' + self.lastname

    
    def __int__(self):
        return self.salary

    
    def __eq__(self,other):
       return self.salary==other.salary   

    
    def __add__(self, other):
        return self.salary + other.salary

    
    def __mul__(self, other):
        return self.salary * other.salary

if __name__ == '__main__':
    Omkar = Employee('Omkar', 'Pathak', 1000)
    Jagdish = Employee('Jagdish','Pathak', 2000)
    print(Omkar)                
    print(Jagdish)              
    print(Omkar + Jagdish)      
    print(Omkar * Jagdish)      
    print(int(Omkar))           
    print(int(Jagdish))         
    print(Omkar==Jagdish)
