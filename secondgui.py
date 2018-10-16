from easygui import *
import sys
while 1:
    msgbox("Hello, world!")
    title = "Sports Survey"
    msg ="What is your favorite sports?"
    
    choices = ["Cricket", "Football", "basketball", "Baseball"]
    choice = choicebox(msg,title , choices)

    # note that we convert choice to string, in case
    # the user cancelled the choice, and we got None.
    msgbox("You chose: " + str(choice), "Survey Result")

    msg = "Do you want play or not"
    title = "Please Confirm"
    if ccbox(msg, title):     # show a Continue/Cancel dialog
        pass  # user chose Continue
    else:
        sys.exit(0)
