import ev3dev.ev3 as ev3
import time

import robot_controller as robo

def main():
    play_sound()

def play_sound():
    ev3.Sound.play("/home/robot/csse120/projects/bockke/Clip_from_Harry_Potter_and_the_Deathly_Hallows_-_P.wav")

main()