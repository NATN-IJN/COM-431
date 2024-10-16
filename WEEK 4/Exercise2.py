class Student:
    def __init__(self, stud_id, name, course):
        self.stud_id = stud_id
        self.name = name
        self.course = course
        self.mark = 0


    def setmark(self, mark):
        if 0 <= mark <= 100:
            self.mark = mark
            return True
        else:
            return False

    def printgrade(self):
        if self.mark >= 70:
            print("First")
        elif 60 <= self.mark >= 69:
            print("2/1")
        elif 50 <= self.mark >= 59:
            print("2/2")
        elif 40 <= self.mark >= 49:
            print("Third")
        else:
            print("Fail")

    def print(self):
        print(f"ID: {self.stud_id}, Name: {self.name}, Course: {self.course}, Mark: {self.mark}")