import turtle


def irma_setup():
    """Creates the Turtle and the Screen with the map background
       and coordinate system set to match latitude and longitude.

       :return: a tuple containing the Turtle and the Screen

       DO NOT CHANGE THE CODE IN THIS FUNCTION!
    """
    import tkinter
    turtle.setup(965, 600)  # set size of window to size of map

    wn = turtle.Screen()
    wn.title("Hurricane Irma")

    # kludge to get the map shown as a background image,
    # since wn.bgpic does not allow you to position the image
    canvas = wn.getcanvas()
    turtle.setworldcoordinates(-90, 0, -17.66, 45)  # set the coordinate system to match lat/long

    map_bg_img = tkinter.PhotoImage(file="images/atlantic-basin.png")

    # additional kludge for positioning the background image
    # when setworldcoordinates is used
    canvas.create_image(-1175, -580, anchor=tkinter.NW, image=map_bg_img)

    t = turtle.Turtle()
    wn.register_shape("images/hurricane.gif")
    t.shape("images/hurricane.gif")

    return (t, wn, map_bg_img)


def irma():
    """Animates the path of hurricane Irma
    """
    (t, wn, map_bg_img) = irma_setup()
    data = []
    time = []
    lat = []
    long = []
    wind = []
    pres = []

    text = open('data/irma.csv', 'r')
    for line in text.readlines()[1:]:
        line = line.strip()
        parts = line.split(",")
        data.append(parts[0])
        time.append(parts[1])
        lat.append(float(parts[2]))
        long.append(float(parts[3]))
        wind.append(int(parts[4]))
        pres.append(int(parts[5]))



    t.up()
    t.hideturtle()

    
    y = lat[0]
    x = long[0]
    t.setx(x)
    t.sety(y)
    t.showturtle()
    t.down()
    t.speed(5)
    


    length = len(lat)
    for i in range(length):
        speed = wind[i]
        
        if speed < 74:
            t.width(1)
            t.pencolor("white")

        elif 74 <= speed <= 95:
            t.width(3)
            t.pencolor("blue")
            t.write("1", font=(20))

        elif 96 <= speed <= 110:
            t.width(5)
            t.pencolor("green")
            t.write("2", font=(20))

        elif 111 <= speed <= 129:
            t.width(7)
            t.pencolor("yellow")
            t.write("3", font=(20))

        elif 130 <= speed <= 156:
            t.width(8)
            t.pencolor("orange")
            t.write("4", font=(20))

        elif speed > 156:
            t.width(11)
            t.pencolor("red")
            t.write("5", font=(20))


        x = long[i]
        y = lat[i]
        t.goto(x, y)

    # close the Screen
    wn.exitonclick()

if __name__ == "__main__":
    irma()
