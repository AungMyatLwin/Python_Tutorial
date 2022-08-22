
#class
class Animal:

    #constructor
    def __init__(self,species,name,age):
        self.species=species
        #private __name
        self.__name=name
        self.age=age
    
    #__ is private to do abstract
    def __abstractclass(self):
        print("abstract  class")

    @property
    #encapsulation getter
    #readonly
    def get_Name(self):
        return self.__name

    #propertymethod.setter
    @get_Name.setter
    def set_name(self,x):
        self.__name=x

    def talk(self):
        self.talking="talking"
        print(f"{self.__name} is little {self.species} and {self.age} and {self.talking}")


    #inherited from animal class
class Cat(Animal):
    #constructor
    def __init__(self, species, name, age,talking):
        #super inherited from parent class
        super().__init__(species, name, age)
        self.talking=talking

    # override the talk function and its called polymorphism
    def talk(self):
        print(f"{self.talking},{self.set_name}")



a=Animal("species","name","age")
a.talking="Talk"
print(a.talking)
a.set_name="Rest"
print(a.get_Name)
a.talk()

cat=Cat("Cat","Tiger","14","Meow")

cat.talk()
cat.set_name="Me ow"
print(cat.get_Name)


# print("Jello")