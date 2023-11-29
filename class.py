class Person:
    num_of_object =0
    def __init__(self, name, age=22 ):
        self.name = name
        self.age = age
        Person.num_of_object +=1
    def __str__(self):
        return print("hello{} you are{} years old".formate(self.name,self.age))
    
def run(self):
    return "{} is talking" .format(self.name)
person1 = Person("Ahmed" , 24)
person2 = Person("Mohammed" , 28)
person3 = Person("Ali")
print(person2.num_of_object)
print(person3.age)

        