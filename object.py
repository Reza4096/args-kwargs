# Using *args and **kwargs to set values of object
# *args receives arguments as a tuple.
# **kwargs receives arguments as a dictionary.

class car(): #defining car class
	def __init__(self,*args): #args receives unlimited no. of arguments as an array
		self.speed = args[0] #access args index like array does
		self.color=args[1]
				
#creating objects of car class
		
audi=car(200,'red')
bmw=car(250,'black')
mb=car(190,'white')
	
print(audi.color)
print(bmw.speed)
print(mb.__dict__)

# With **kwargs
class car2(): #defining car class
    def __init__(self,**kwargs): #args receives unlimited no. of arguments as an array
        self.speed = kwargs['s'] #access args index like array does
        self.color = kwargs['c']
                 
#creating objects of car class
         
audi=car2(s=200,c='red')
bmw=car2(s=250,c='black')
mb=car2(s=190,c='white')
    
print(audi.color)
print(bmw.speed)
print(mb.__dict__)