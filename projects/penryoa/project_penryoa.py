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
- Just for fun, the LED's will be red on the "Everybody clap your hands!" command.

"""

import ev3dev.ev3 as ev3
import time
import math
import penryoa_robot_controller as robo
import tkinter
from tkinter import ttk
import penryoa_mqtt_remote_method_calls as com

"""
NOTE TO SELF: Make com and robo go to my own copies in my folder.
"""
robot = robo.Snatch3r

"""
                                                    PC remote
"""
def main():
    client = com.MqttClient()
    client.connect_to_ev3()

    root = tkinter.Tk()
    root.title("Cha Cha Slide")

    main_frame = ttk.Frame(root, padding=20, relief='raised')
    main_frame.grid()

    slide_left_button = ttk.Button(main_frame, text="Slide to the left!")
    slide_left_button.grid(row=1, column=0)
    slide_left_button['command'] = lambda: slide_left(client)
    root.bind('<Left>', lambda event: slide_left(client)

    slide_right_button = ttk.Button(main_frame, text="Slide to the right!")
    slide_right_button.grid(row=1, column=2)
    slide_right_button['command'] = lambda: slide_right(client)
    root.bind('<Right>', lambda event: slide_right(client)

    one_hop_button = ttk.Button(main_frame, text="One hop this time.")
    one_hop_button.grid(row=0, column=1)
    one_hop_button['command'] = lambda: one_hop(client)
    root.bind('<Up>', lambda event: one_hop(client)

    take_back_button = ttk.Button(main_frame, text="Take it back, now, y'all.")
    take_back_button.grid(row=2, column=1)
    take_back_button['command'] = lambda: take_it_back(client)
    root.bind('<Down>', lambda event: take_it_back(client)

    freeze_clap_button = ttk.Button(main_frame, text="Clap your hands!")
    button.grid(row=0, column=0)
    button['command'] = lambda: c(client)
    root.bind('<Space>', lambda event: c(client)

    button = ttk.Button(main_frame, text="")
    button.grid(row=0, column=0)
    button['command'] = lambda: c(client)
    root.bind('<Enter>', lambda event: c(client)



"""
                                    Defining the functions that the buttons call
"""

def slide_left(client):
    print('Slide to the left')
    client.send_message(slide_to_left)

def left_stomp(client):
    print("Left foot, let's stomp!")
    client.send_message(left_stomp)

def slide_right(client):
    print('Slide to the right')
    client.send_message(slide_to_right)

def right_stomp(client):
    print("Right foot, let's stomp!")
    client.send_message(right_stomp)

def one_hop(client):
    print('One hop this time')
    client.send_message(one_hop)

def two_hops(client):
    print('Two hops')
    client.send_message(two_hops)

def freeze_clap(client):
    print('FREEZE... Now everybody clap your hands!')
    client.send_message(freeze_clap)

def cha_cha_smooth(client, turns_to_cha_cha):
    print("Cha cha real smooth.")
    client.send_message("cha_cha_real_smooth", [int(turns_to_cha_cha.get())])

def take_it_back(client):
    print("Take it back, now, y'all.")

