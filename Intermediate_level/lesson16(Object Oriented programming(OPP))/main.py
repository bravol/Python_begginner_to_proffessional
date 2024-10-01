from turtle import Turtle, Screen

# creating a new object from a blueprint
timmy = Turtle()
print(timmy) #object
timmy.shape('turtle')
timmy.color('coral')
timmy.forward(100)

my_screen = Screen() # object
print(my_screen.canvheight) # attributes of object
# methods of objects
my_screen.exitonclick()