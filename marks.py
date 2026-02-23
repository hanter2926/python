class Student:
    def _init_(self, name, marks):
        self.name = name
        self.marks = marks

    def show_details(self):
        print("Name:", self.name)
        print("Marks:", self.marks)

s1 = Student("vikram", 85)
s1 = student("vikram pal", 90)
s1.show_details()