# The special syntax *args
# in function definitions in python is used to pass a variable number of arguments to a function.
# It is used to pass a non-key worded,
# variable-length argument list. 

def myFun(*args):
    for arg in args:
        print(arg)

myFun('Hello', 'python', 'is', 'fun')