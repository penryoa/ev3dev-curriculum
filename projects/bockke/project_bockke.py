import ev3dev.ev3 as ev3
import time

import robot_controller as robo

def main():
    play_sound()




def pick_up_alien():
    pass


#this is for the shutdown of the theme song
class DataContainer(object):
    """ Helper class that might be useful to communicate between different callbacks."""

    def __init__(self):
        self.running = True
dc = DataContainer()
btn = ev3.Button()

def play_sound():
    while dc.running:
        ev3.Sound.play("/home/robot/csse120/assets/sounds/xfilestheme.wav")
        btn.process()  # This command is VERY important when using button callbacks!
        time.sleep(0.01)  # A short delay is important to allow other things to happen.
        btn.on_backspace = lambda state:handle_shutdown(state,dc)
        print("Goodbye!")
        ev3.Sound.speak("Goodbye").wait()

def handle_shutdown(button_state, dc):
    if button_state:
        print('back')
        dc.running = False


main()