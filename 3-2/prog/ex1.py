class Vignan:
    def __init__(self):
        print("Vignan College")
class Child(Vignan):
    def __init__(self):
        print("Child class")
    def display(self):
        print("Hyderabad")
o=Child()
o.display()
