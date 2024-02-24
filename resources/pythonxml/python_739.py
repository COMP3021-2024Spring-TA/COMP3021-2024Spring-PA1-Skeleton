


class Person(object):
    def __init__(self, name):
        self.name = name
        self.__education = 'Engineering'         

    def displayInfo(self):
        name = self.name
        education = self.__education             
        print('My name is', name, 'and I have completed my', education)

if __name__ == '__main__':
    myObj = Person('Omkar')
    myObj.displayInfo()
    print(myObj.name)                           
    
    print(myObj._Person__education)             
                                                
