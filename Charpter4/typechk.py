def displayNnmType(num):
    print("{} is ".format(num),end="")
    if isinstance(num, (int, float, complex)):
        print("a number of type: {}".format(type(num)))
        print("a number of type: {}".format(type(num).__name__))
    else:
        print("not a number at all!")
displayNnmType(99)
displayNnmType(1.9903)
displayNnmType(-5.2+1.9j)
displayNnmType("xxxx")

import types
def displayNumTyper2(num):
    print("{} is ".format(num),end="")
    if isinstance(num, int)
        print("an interger")

displayNumTyper2(88)