import json
import os
class Student:
  def __init__(self,id,name,age):
    self.id=id
    self.name=name
    self.age=age
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
