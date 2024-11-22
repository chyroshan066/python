class A:
    def show(self):
        print("Shown in class A")

class B(A):
    def show(self):
        print("Shown in class B")

a = B()
print(a.show())