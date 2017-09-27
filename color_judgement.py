# import libraries that we need
from psychopy import visual, core, event, logging

# only log critical errors thrown by psychopy
logging.console.setLevel(logging.CRITICAL)


def create_experiment_window(color):
    '''create window in which we run the experiment'''
    window = visual.Window([1024, 768], allowGUI=True, fullscr=False,
                           units='pix', color=color, colorSpace='rgb255')
    return window


def create_square(window, width, height, color):
    square = visual.Rect(window,
                         width=300, height=300,
                         lineColor=color,  # line color in rgb values
                         lineWidth=1,  # width of line surrounding the stimulus
                         fillColor=color,  # fill color in rgb values
                         fillColorSpace='rgb255',
                         interpolate=True,
                         opacity=1,  # no opacity
                         pos=[0, 0],  # center it in the middle of the screen
                         autoLog=False)
    return square


def print_color(color):
    print 'The color indicated after pressing the spacebar was: %s' % color


def main(window, square, color):
    # prepare cycling
    n = -1
    keynotpressed = True

    # do this until a key is pressed
    while keynotpressed:
        square.draw()  # draw the stimulus to the buffer
        mywin.flip()  # show the buffer on the screen

        # update fill color of stimulus
        new_color = [color[0], color[1], n]
        square.fillColor = new_color
        square.lineColor = new_color
        # increment of the rgb value we are going to change
        n = n + 0.5
        # make sure the changed rgb value stays within the allowed range
        if n > 255:
            n = 1

        # check whether the space bar was pressed
        for keys in event.getKeys(timeStamped=True):
            if keys[0] in ['space']:
                keynotpressed = False
                print_color(new_color)


if __name__ == '__main__':
    color = [255, 153, 0]
    # create a window to run experiments in
    mywin = create_experiment_window('black')

    # create clock to keep track of time (not used yet)
    trialClock = core.Clock()

    # create a square in the experiment window
    square = create_square(mywin, 300, 300, color)

    main(mywin, square, color)
    mywin.close()  # close the window
    core.quit()  # end the program
