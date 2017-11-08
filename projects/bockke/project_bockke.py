import ev3dev.ev3 as ev3
import time

import robot_controller as robo

def main():
    play_sound()

def play_sound():
    ev3.Sound.play("/home/robot/csse120/assets/sounds/dobby.wav")
main()

def pick_up_sock():
    pass