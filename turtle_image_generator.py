from PIL import Image
import turtle
import imghdr
import sys


screen = turtle.Screen()
screen.colormode(255)
turtle.bgcolor('grey')
turtle.tracer(100)

image = ""
file = 'C:/Users/ghodg/Desktop/cool.jpg'

# coordinates of the first square that is created
four_corners = [[5, 5], [0, 5], [0, 0], [5, 0]]

#open_image = input("Insert the file location here: \n")
image = Image.open(file)

if imghdr.what(file) == "png":
    image.convert('RGB')
    print("Image converted")
elif imghdr.what(file) == "jpeg":
    print("Good jpeg")
else:
    print("This image type cannot be converted.\n"
          "Please use either .png or .jpeg image formats.")


# resize image to under 600 pixels
if max(image.size) > 600:
    size = (600, 600)
    image.thumbnail(size, Image.ANTIALIAS)


old_size = image.size
new_size = (600, 600)
newImage = Image.new("RGB", new_size, (255, 255, 255))
newImage.paste(image, ((new_size[0]-old_size[0])//2,
                       (new_size[1]-old_size[1])//2))

x_image, y_image = newImage.size  # store image dimensions
pixImage = newImage.transpose(Image.FLIP_LEFT_RIGHT)
pixels = pixImage.load()


def create_turtle(x, y):
    """
    Create the turtle pen with specific attributes
    ==============================================

    - Set speed and pen color
    - Direction is set default due east
    - Pen is returned in list with x and y coordinates
    """
    t = turtle.Pen()
    t.speed(8)
    t.pencolor("white")
    return [t, x, y]


def check_direction(turt, dist):
    """[summary]
    Check turtle direction and move pen
    [description]
    Changes the coordinates of the turtle based on direction and distance
    Proceeds to move pen specified distance
    """
    direction = turt[0].heading()
    if direction == 0:
        turt[1] += dist
        turt[0].forward(dist)
    elif direction == 90:
        turt[2] += dist
        turt[0].forward(dist)
    elif direction == 180:
        turt[1] -= dist
        turt[0].forward(dist)
    elif direction == 270:
        turt[2] -= dist
        turt[0].forward(dist)


def square_maker(turt, i):
    """[summary]
    Check if turtle has created a new corner and if not, run default motion
    [description]
    For-loop checks if turtle has created a new corner of the overall square
    Each corner corresponds with cartesian coordinate quadrant
    """
    # set pen
    p = turt[0]

    # check each time turtle moves if large square corner was made
    for i in range(4):
        x = turt[1]
        y = turt[2]

        # first corner
        if x == 5 + four_corners[0][0] and y == 5 + four_corners[0][1]:
            four_corners[0][0] = x
            four_corners[0][1] = y
            p.left(90)
            check_direction(turt, 5)
            p.left(90)
            check_direction(turt, 10)
            break
        # second corner
        elif x == four_corners[1][0] - 5 and y == 5 + four_corners[1][1]:
            four_corners[1][0] = x
            four_corners[1][1] = y
            p.left(90)
            check_direction(turt, 5)
            p.left(90)
            check_direction(turt, 10)
            break
        # third corner
        elif x == four_corners[2][0] - 5 and y == four_corners[2][1] - 5:
            four_corners[2][0] = x
            four_corners[2][1] = y
            p.left(90)
            check_direction(turt, 5)
            p.left(90)
            check_direction(turt, 10)
            break
        # forth corner
        elif x == four_corners[3][0] + 5 and y == four_corners[3][1] - 5:
            four_corners[3][0] = x
            four_corners[3][1] = y

            # last corner in each large square; dictates different turtle directions
            for _ in range(2):
                p.left(90)
                check_direction(turt, 5)
                p.left(90)
                check_direction(turt, 5)
                p.left(90)
                check_direction(turt, 5)
                p.end_fill()
                getRGB(turt)
                p.begin_fill()
                check_direction(turt, 5)
            break

        # default turtle movements if small square being created is not a corner
        if i == 3:
            p.left(90)
            check_direction(turt, 5)
            p.end_fill()
            getRGB(turt)
            p.begin_fill()
            check_direction(turt, 5)
        else:
            p.left(90)
            check_direction(turt, 5)


def getRGB(turt):
    """[summary]
    Get RGB value of pixel nearest to turtle's coordinates
    [description]
    Using pixel map loaded from image data, save the RGB value of the pixel
    Change pen fill color
    """
    r, g, b = pixels[x_image/2 - turt[1], y_image/2 - turt[2]]
    turt[0].fillcolor(r, g, b)


def save_image():
    """[summary]
    Ask to save replicated image and exit program
    [description]
    Ask to save image as a postscript file
    Ask to replicate another image
    Finally, exit program
    """
    save = input("Do you want to save this piece of art as a postscript file? (yes or no)\n")

    if save == "yes":
        # get created image
        cv = turtle.getcanvas()
        ps_file_name = input("What do you want to save this beauty as?\n")
        cv.postscript(file=ps_file_name + ".ps", colormode='color')
        print("Image saved as a postscript file!")

        # close turtle window and exit
        turtle.bye()
        turtle.done()
        sys.exit()
    elif save == "no":
        turtle.bye()
        turtle.done()
        sys.exit()
    else:
        # repeat input
        print("I beg your pardon?")
        save_image()


def control_turtle():
    """
    Main function that creates first square and runs loop to call square_maker()
    ============================================================================

    - Creates first square at (0,0) and second square due south
    - Moves on to third square where it institutes default motion
    - Once image is replicated, it calls save_image()
    """
    # create the turtle and set variables
    turt = create_turtle(0, 0)
    p = turt[0]
    x = turt[1]
    y = turt[2]

    # create first square
    getRGB(turt)
    p.begin_fill()

    for i in range(3):
        check_direction(turt, 5)
        p.left(90)
    p.end_fill()

    # create second square
    getRGB(turt)
    p.begin_fill()
    check_direction(turt, 10)
    p.left(90)
    check_direction(turt, 5)
    p.left(90)
    check_direction(turt, 5)
    p.left(90)
    check_direction(turt, 5)
    p.end_fill()

    # begin third square
    check_direction(turt, 5)
    getRGB(turt)
    p.begin_fill()

    # default motion begins
    while (-y_image/2 < y < y_image/2):
        square_maker(turt, i)

        # make sure turtle coordinates are saved
        x = turt[1]
        y = turt[2]
        print(x)
        print(y)

    save_image()


if __name__ == "__main__":
    control_turtle()


s = 'saassssssss'
counter = 4
i = 's'
for i in s:

b = s[:1]
a = sum([1 for x in b if x == i])


