name = input("Enter name: ")
marks = int(input("Enter marks: "))

class student:
     

    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        
print(f"I am {name} and i got {marks}")