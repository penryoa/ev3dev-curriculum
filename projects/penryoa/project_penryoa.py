"""

 ---------  ----      ----  ----     ----  ----      ---
 ---------  ----      ----   ----   ----   ----     -----
 ---   ---  ----      ----    ---- ----    ----    --   --
 ---   ---  ----      ----     -------     ----   ---------
 ---------  --------  ----      -----      ----  ---     ---
 ---------  --------  ----       ---       ---- ---       ---

GOAL:
The goal of this project is to get the robot to the Cha Cha Slide! Should be fun.
(It'd be helpful to be familiar with the song.)
- There is a PC remote that has buttons saying "Slide to the left!", "Slide to the right!", etc.
    set so that when those buttons are pressed, the robot will go the indicated direction or do
    the indicated action.
- When the button "Cha Cha real smooth" is pressed, the robot will play a sound snippet
    of the song and move around a bit, mainly left and right.
- User can input a number of seconds to do the "Cha Cha real smooth" command. Because the robot is slow,
    If the user inputs anything under ten seconds, it will be accounted as ten. The robot has got to
    cha cha real smooth, you know? To do this to my satisfaction, the robot needs a bit of time!
- Just for fun, the LED's will go off on the "Everybody clap your hands!" command.

"""

import ev3dev.ev3 as ev3
import time
import math
import robot_controller as robo
import tkinter
from tkinter import ttk
import mqtt_remote_method_calls as com

"""
NOTE TO SELF: Make com and robo go to my own copies in my folder.
"""
robot = robo.Snatch3r

# Making the PC remote:
def main():
    client = com.MqttClient()
    client.connect_to_ev3()

    root = tkinter.Tk()
    root.title("Remote")

    main_frame = ttk.Frame(root, padding=20, relief='raised')
    main_frame.grid()

    forward_button = ttk.Button(main_frame, text="Forward")
    forward_button.grid(row=2, column=1)
    forward_button['command'] = lambda: go_forward(mqtt_client, left_speed_entry, right_speed_entry)
    root.bind('<Up>', lambda event: go_forward(mqtt_client, left_speed_entry, right_speed_entry))




def slide_left(client):
    print('Slide to the left!')
