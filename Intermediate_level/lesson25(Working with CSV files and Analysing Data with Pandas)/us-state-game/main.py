import turtle

screen =turtle.Screen()

screen.title('U.S. State Game')
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
# create a pop-up box
answer_state = screen.textinput(title='Guess the state', prompt="What's another state's name?")
print(answer_state)





# screen.exitonclick()
# turtle.mainloop()