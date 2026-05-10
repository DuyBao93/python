# class Person:
#     def __init__(self, id, name, age, male):
#         print("Class person được khởi tạo với id = %d" %(id))
#         self.name, self.age, self.male = name, age, male
    
#     def getName(self):
#         print("Name: %s" %(self.name))
    
#     def getAge(self):
#         print("Age: %d" %(self.age))
    
#     def getMale(self):
#         print("Male: %s" %(self.male))
    
#     def __del__(self):
#         print('Class Person được hủy')
#         del self.name,self.age,self.male

# person = Person(1, 'Vu Thanh Tai', 22, True)
# person.getName()
# person.getAge()
# person.getMale()
class Foo:
    __name = "default"
    # Khai báo thuộc tính ở chuẩn private
    def __init__(self, name):
        print("Class foo được khởi tạo với")
        self.__name = name
    # Khai báo phương thức ở chuẩn private
    def __getName(self):
        # gọi thành phần trong class
        print(self.__name)
    # khai báo một phương thức ở dạng public để gọi thành phần private
    def get(self):
        self.__getName()

# gọi thành phần ngoài class
#print(Foo().__name) # 'Foo' object has no attribute '__name'
#Foo().__getName() # 'Foo' object has no attribute '__getName'
# Foo().get() # Foo

class Bar(Foo):
    __name = "default"
    def __init__(self, name):
        print("Class bar được khởi tạo với")
        self.__name = name
    def getNameinFoo(self):
        print(self.__name)
        self.get()

#test

foo = Foo("foo nha")
foo.get()
Foo("foo").get()
bar = Bar("Bar")
bar.getNameinFoo()