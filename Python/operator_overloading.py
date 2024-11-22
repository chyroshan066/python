# a = 5
'''a = "Ram"
# b = 7
b = "Shyam"
# print(int.__add__(a, b))
print(str.__add__(a, b))'''

class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        return Student(m1, m2)

    def __str__(self):
        return f"({self.m1}, {self.m2})"

s1 = Student(59, 65)
s2 = Student(66, 74)
# s3 = s1 + s2
s3 = Student.__add__(s1, s2)
print(s3.m2)
print(s1)  # Prints the address of s1 instead of value when "__str__()" magic method is not overridden