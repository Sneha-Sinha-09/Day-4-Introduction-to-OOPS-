#1 Finding nearest palindrome
import sys
def nearest_palindrome(num):
    for i in range(num+1,sys.maxsize):
        if str(i)==str(i)[::-1]:
            return i
print(nearest_palindrome(99))
print(nearest_palindrome(1221))


#2 Calculating maximum visited speciality in a hospital
def max_visited_speciality(list1,medical_speciality):
    max_visit=0
    P=list1.count("P")
    E=list1.count("E")
    O=list1.count("O")
    if P>E and P>O:
        speciality=medical_speciality["P"]
    elif E>O and E>P:
        speciality=medical_speciality["E"]
    else:
        speciality=medical_speciality["O"]
    return speciality
        
medical_speciality={"P":"Pediatrics","O":"Orthopedics","E":"ENT"}
list1=list(map(str,input().split(",")))
speciality=max_visited_speciality(list1,medical_speciality)
print(speciality)




#4
class Example:
    def __init__(self,num):
        self.num=num
    def set_num(self,num):
        self.num=num
    def get_num(self):
        return self.num
    
obj=Example(10)
print(obj.get_num())
obj.set_num(15)
print(obj.get_num())


#5
class Customer:
    def __init__(self,id):
        self.id=100

c1=Customer(200)
print(c1.id)

class Customer:
    def __init__(self,id):
        self.id=id

c1=Customer(200)
print(c1.id)



#6
class Book:
    def __init__(self):
        self.title=None
my_fav=Book()
my_fav.title="Head First Programming"
your_fav=Book()
your_fav.title="Learning Python the hard way"

my_fav.title="Learning Python"

print("My favourite is",my_fav.title)
print("Your's is",your_fav.title)
        
            



















