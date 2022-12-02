# Here, we are passing *args and **kwargs as an argument in the myFun function. 
def myFun(arg1, arg2, arg3):
	print("arg1:", arg1)
	print("arg2:", arg2)
	print("arg3:", arg3)

# Now we can use *args or **kwargs to
# pass arguments to this function :
args = ("reza", "was", "here")
myFun(*args)

kwargs = {"arg1": "reza", "arg2": "was", "arg3": "here"}
myFun(**kwargs)


# pass to *args and *kwargs :
def myFun(*args, **kwargs):
	print("args: ", args)
	print("kwargs: ", kwargs)

myFun('reza', 'was', 'here', first="reza", mid="was", last="here")
