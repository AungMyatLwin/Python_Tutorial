


class Madlib:
    def __init__(self,name,age,favourite_color):
        self.name=name
        self.age=age
        self.fav=favourite_color
        
    @property
    def get_color(self):
        return self.fav 

    @get_color.setter
    def update_color(self,new_color=" "):
        self.fav=new_color

    def madlib(self):
        return f"My name is {self.name} and my age is {self.age} and I like {self.fav}."

    

def main():
        print("Madlib game is starting")
        name=input("Enter your name?: ")
        age=int(input("Enter your age?: "))
        favC=input("Enter your Favourite Color?: ")
        mdl=Madlib(name,age,favourite_color=favC)
        print(mdl.madlib())
        print("before")
        print(mdl.fav)
        print(mdl.get_color)
        print("update Color")
        new_col="Green"
        mdl.update_color=new_col
        print(mdl.fav)
        print(mdl.get_color)

def array():
    luckyNumber={4,8,15,16,23,42}
    luckyNumber=list(luckyNumber)
    luckyNumber[1]=3
    print(luckyNumber[1])

def empty_arr():
    friends=[""]*11
    friends[0]="Jim"
    print(friends)


def sayHi(name=""):
    print("Hi"+name)


def pows(n=0,m=0):
   temp=0
   for i in range(0,m):
    temp+=n
    n=temp
    print(temp)

def cube(n):
    return n*n*n


if __name__=="__main__":
    print(2**10)
    pows(2,10)
    print(cube(5))

    