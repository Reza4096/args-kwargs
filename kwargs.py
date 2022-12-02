# The special syntax **kwargs in function definitions in python is used to pass a keyworded,
# variable-length argument list. We use the name kwargs with the double star.

def myFun(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))

myFun(first='Reza', mid='Was', last='Here')