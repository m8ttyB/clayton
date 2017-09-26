# import libraries that we need
from psychopy import visual, core, event, logging

# only log critical errors thrown by psychopy
logging.console.setLevel(logging.CRITICAL)

# create window in which we run the experiment
def create_experiment_window(color):
    window = visual.Window([1024,768], allowGUI=True, fullscr=False,
                            units='pix', color=color, colorSpace='rgb')
    return window


def create_square(window, width, height, color):
    square = visual.Rect(window,
                        width=300, height=300,
                        lineColor=color, # line color in rgb values
                        lineWidth=1, # width of line surrounding the stmimulus
                        fillColor=color, # fill color in rgb values
                        fillColorSpace='rgb', # color space of fill color
                        interpolate=True,
                        opacity=1, # no opacity
                        pos=[0,0], # center it in the middle of the screen
                        autoLog=False
                        )
    return square


def print_color(color):
    print 'The color indicated after pressing the spacebar was: %s' % color


def main(window, square, color):
    # prepare cycling
    n = -1
    keynotpressed = True

    # do this until a key is pressed
    while keynotpressed:
        new_color = [color[0], color[1], n]
        square.fillColor = new_color # update fill color of stimulus
        square.lineColor = new_color # update line color of stimulus
        n = n + 0.005 # increment of the rgb value we are going to change
        if n > 1: n = 1 # make sure the changed rgb value stays within the allowed range

        # check whether the space bar was pressed
        for keys in event.getKeys(timeStamped=True):
            if keys[0]in ['space']:
                keynotpressed = False
                print_color(new_color)
        square.draw() # draw the stimulus to the buffer
        mywin.flip() # show the buffer on the screen


if __name__ == '__main__':
    # color = [-1,1,0] # green
    color = [1, 0.294117647058824, -1] # orange
    mywin = create_experiment_window('black')
    # create clock to keep track of time (not used yet)
    trialClock = core.Clock()

    # square = create_square(mywin, 300, 300, [-1,1,0])
    square = create_square(mywin, 300, 300, color)

    main(mywin, square, color)
    mywin.close() # close the window
    core.quit() # end the program
