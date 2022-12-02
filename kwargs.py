# The special syntax **kwargs in function definitions in python is used to pass a keyworded,
# variable-length argument list. We use the name kwargs with the double star.

def myFun(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))

myFun(first='Reza', mid='Was', last='Here')

# to illustrate  **kwargs for a variable number of keyword arguments with one extra argument
def myFun2(arg1, **kwargs):
	for key, value in kwargs.items():
		print("%s == %s" % (key, value))

myFun2("Hi", first='Reza', second='Was', third='Here')
