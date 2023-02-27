class student:
    def __init__(self,name):
        self.name=name
    def display(self):
        print("student name :",self.name)
class roll(student):
    def __init__(self,name,roll):
        super().__init__(name)
        self.roll=roll
    def display(self):
        super().display()
        print("roll number :",self.roll)
class marks(roll):
    def __init__(self,name,roll,marks):
        super().__init__(name,roll)
        self.marks=marks
    def display(self):
        super().display()
        print("marks :",self.marks)
o=marks("bharath","20891A6616",100)
o.display()
