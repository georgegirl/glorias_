class Georges():


    num_of_limbs= 4

    def __init__(self, breed: str, colour: str, weight:int):
        self.breed = breed
        self.colour = colour
        self.weight = weight


    def __str__(self):
        return self.breed

    def __add__(self, other):
        if isinstance(other, Georges):

            return self.weight + other.weight
        raise TypeError("expected type of dog but got %" % type(other))

# these are intance methods
    def run(self):
        return f'This dog with {self.weight}kg is running'

    def shape(self):
        return f"The Dog of {self.breed}  breed's tend to look fat."



#0
dog1 = Georges("german shepherd", "black", 20)
#1
dog2 = Georges("bull dog", "brown", 40)


# print(dog1 +dog2) # this is a magic method

# print(dog1) #this prints out 0
# print(dog1.breed, dog1.colour, dog1.weight)


# print(Georges.num_of_limbs) # this prints out the 

 

#these prints out the instant method
# print(dog1.run())
# print(dog1.shape())

