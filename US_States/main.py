import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
# I can set up a new shape, using an image

screen.addshape(image)

turtle.shape(image)

answer_state = screen.textinput(title="Guess a state name", prompt="Guess another state")



# # Prints the x and y coord of location where I click
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# # Listens on mouseclick and calls function
# turtle.onscreenclick(get_mouse_click_coor)
#
# # Keeps the turtle (Screen) running. Alternative of exit on click, which doesn't make sense here (obviously)
turtle.mainloop()

