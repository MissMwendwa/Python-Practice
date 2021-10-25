#import the turtle packag
import turtle

#lets create a turtle object
pen = turtle.Turtle()

#defining the method to draw a curve
def curve():
    for i in range(300):
        #defining the step by step curve
        pen.right(1)
        pen.forward(1)

#defining method to raw the full heart
def heart():
    #add the fill color
    pen.fillcolor('blue')

    #starting to fill the color
    pen.begin_fill()

    #Drawing the left line
    pen.left(150)
    pen.forward(113)

    #drawing the left curve
    curve()
    pen.left(120)

    #drawing the right curve
    curve()

    #drwaing the right line
    pen.forward(112)

    #ending the filling of the color
    pen.end_fill()

#Defining the method to write text
def txt():

    #moving the turtle up to the air
    pen.up()

    #move turtle to a given position
    pen.setpos(-68,95)

    #move the turtle to the ground
    pen.down()

    #setting the text color to lightgreen
    pen.color('lightgreen')

    #writing the specific text to in the specified shape
    pen.write('Gloria sycology', font=("Verdana", 12, "bold"))

#drawing the heart
heart()

#writing the text
txt()

#hiding the turtle
pen.ht()


