import json
import os
class Student:
  def __init__(self,id,name,age):
    self.id=id
    self.name=name
    self.age=age
def set_name(self,name):
  if name.isalpha():
    self.__name==name
  else:
    print("invalid name! only letters allowed")
 def set_name(self,age):
  if age > 0 age <= 120:
    self.__age==age
  else:
    print("invalid age! must between  and 120")
    def get_name(self):
      return self.name
class StudentManager:
  def __init__(self):
    self.students=[]
  def add_student(self,student):
    self.students.append(student)
  def display(self):
    for s in self.students:
    print("ID:"s.id,"Name:",s.name,"Age:", s.age)
   
s1=Student(1,"ABCD",18)
s1.display()
s1.set_name("AB")
print(s1.get_name())
