import ev3dev.ev3 as ev3
import time

import robot_controller as robo
import tkinter
from tkinter import ttk
import mqtt_remote_method_calls as com
from PIL import Image, ImageTk





def main():
    buttons()


def buttons():
    mqtt_client = com.MqttClient()
    mqtt_client.connect_to_ev3()

    root = tkinter.Tk()
    root.title("Let's Get Some Aliens")

    main_frame = ttk.Frame(root, padding=110, relief='raised')
    main_frame.grid()

    imageFile = "alien.jpg"
    image1 = ImageTk.PhotoImage(Image.open(imageFile))

    find_them_button = ttk.Button(main_frame, text="Find Them", image = image1)
    find_them_button.grid(row=1, column=1)
    find_them_button['command'] = lambda: find_them(mqtt_client)
    root.bind('<f>', lambda event: find_them(mqtt_client))

    grab_them_button = ttk.Button(main_frame, text="Grab Them")
    grab_them_button.grid(row=8, column=0)
    grab_them_button['command'] = lambda: grab_them(mqtt_client)
    root.bind('<g>', lambda event: grab_them(mqtt_client))

    place_them_button = ttk.Button(main_frame, text="Put Them Down")
    place_them_button.grid(row=9, column=0)
    place_them_button['command'] = lambda: place_them(mqtt_client)
    root.bind('<p>', lambda event: place_them(mqtt_client, ))

    background_music_button = ttk.Button(main_frame, text="Play Tunes")
    background_music_button.grid(row=10, column=0)
    background_music_button['command'] = lambda: play_tunes(mqtt_client)
    root.bind('<t>', lambda event: play_tunes(mqtt_client))

    forward_button = ttk.Button(main_frame, text="Forward")
    forward_button.grid(row=4, column=1)
    forward_button['command'] = lambda: go_forward(mqtt_client, 600, 600)
    root.bind('<Up>', lambda event: go_forward(mqtt_client, 600, 600))

    left_button = ttk.Button(main_frame, text="Left")
    left_button.grid(row=5, column=0)
    left_button['command'] = lambda: turn_left(mqtt_client, 600)
    root.bind('<Left>', lambda event: turn_left(mqtt_client, 600))


    stop_button = ttk.Button(main_frame, text="Stop")
    stop_button.grid(row=5, column=1)
    stop_button['command'] = lambda: stop(mqtt_client)
    root.bind('<space>', lambda event: stop(mqtt_client))


    right_button = ttk.Button(main_frame, text="Right")
    right_button.grid(row=5, column=2)
    right_button['command'] = lambda: turn_right(mqtt_client, 600)
    root.bind('<Right>', lambda event: turn_right(mqtt_client, 600))


    back_button = ttk.Button(main_frame, text="Back")
    back_button.grid(row=6, column=1)
    back_button['command'] = lambda: go_backward(mqtt_client, 600, 600)
    root.bind('<Down>', lambda event: go_backward(mqtt_client, 600, 600))


    # Buttons for quit and exit
    q_button = ttk.Button(main_frame, text="Quit")
    q_button.grid(row=7, column=2)
    q_button['command'] = (lambda: quit_program(mqtt_client, False))

    e_button = ttk.Button(main_frame, text="Exit")
    e_button.grid(row=8, column=2)
    e_button['command'] = (lambda: quit_program(mqtt_client, True))


    root.mainloop()


def find_them(mqtt_client):
    print("Finding Them")
    mqtt_client.send_message("seek_beacon")


def grab_them(mqtt_client):
    print("Grabbing Them")
    mqtt_client.send_message('arm_up')


def place_them(mqtt_client):
    print("Placing Them")
    mqtt_client.send_message('arm_down')


#This will now control the robot after it's found an alien
def go_forward(mqtt_client, left_speed_entry, right_speed_entry):
    print("Going Forward")
    mqtt_client.send_message("go_forward", [int(left_speed_entry), int(right_speed_entry)])


def stop(mqtt_client):
    print("Stop")
    mqtt_client.send_message("stop")


def go_backward(mqtt_client, left_speed_entry, right_speed_entry):
    print("Going Backward")
    mqtt_client.send_message("go_backward", [int(left_speed_entry), int(right_speed_entry)])


def turn_left(mqtt_client, right_speed_entry):
    print("Turning Left")
    mqtt_client.send_message("turn_left", [int(right_speed_entry)])


def turn_right(mqtt_client, left_speed_entry):
    print("Turning Right")
    mqtt_client.send_message("turn_right", [int(left_speed_entry)])


def play_tunes(mqtt_client):
    print('Playing Tunes')
    mqtt_client.send_message("play_tunes")


def quit_program(mqtt_client, shutdown_ev3):
    if shutdown_ev3:
        print("Shutdown")
        mqtt_client.send_message("shutdown_alien")
    mqtt_client.close()
    exit()


main()