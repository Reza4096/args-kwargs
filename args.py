# The special syntax *args
# in function definitions in python is used to pass a variable number of arguments to a function.
# It is used to pass a non-key worded,
# variable-length argument list. 

def myFun(*args):
    for arg in args:
        print(arg)

myFun('Hello', 'python', 'is', 'fun')


# to illustrate *args with a first extra argument

def myFun2(arg1, *argv):
    print("First argument :", arg1)
    for arg in argv:
        print("Next argument through *argv :", arg)

myFun2('Hello', 'python', 'is', 'fun')