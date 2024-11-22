a = 3  # global

def fun():
    a = 2  # nonlocal
    def run():
        nonlocal a  #This doesn't allocates new memory but instead access the outer function variable. In order to access the nonlocal variable inside the function of the function/scope, we use "nonlocal" keyword
        # a = 1  # local
        print(a)
    run()
    # print(a)

fun()