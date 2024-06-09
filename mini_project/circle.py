import turtle as turtle

def draw_circles (n ):
    
    

    circles_drawn = 0 # number of circles drawn so far
    leo = turtle . Turtle ()
    window = turtle . Screen ()
    while circles_drawn < n :
        leo.width(4)
        leo.color("black", "red")
        leo.begin_fill()


        # while we haven ’t drawn n circles
        leo . goto ( circles_drawn * 50 , 0) # move the turtle
        leo . down () # put the turtle ’s pen down
        leo . circle (20) # draw a circle of radius 20 pixels
        leo . up () # pick up the turtle ’s pen
        # add 1 to the number of circles drawn
        circles_drawn = circles_drawn + 1
        leo.end_fill()
    window . mainloop ()


def num():
    x=int(input("enter how many circular: "))
    return x

draw_circles (num() )
