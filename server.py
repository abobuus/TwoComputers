from tkinter import *
import tkinter as tk
import socket
from pathlib import Path

print('Enter your IP-address: ')
ip = input()
print('Enter port: ')
port = int(input())

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((ip, port))

print(1)

server.listen(2)

user, address = server.accept()

print(2)


def on_button_click():
    button.config(image=get_next_image())


def get_next_image():
    return next(NEXT_IMAGE)


print(3)


def next_image_generator():
    photo_list = [
        tk.PhotoImage(file=Path("assets", "cat1.png")),
        tk.PhotoImage(file=Path("assets", "cat2.png")),
        tk.PhotoImage(file=Path("assets", "cat3.png")),
        tk.PhotoImage(file=Path("assets", "cat4.png")),
        tk.PhotoImage(file=Path("assets", "boom.png"))
    ]

    while True:
        yield from photo_list


print(4)


NEXT_IMAGE = next_image_generator()

root = Tk()
root.geometry('750x750')
root.resizable(False, False)

print(5)

button = Button(root, image=get_next_image())
button.pack()

print(6)

while True:
    root.update()
    print(7)
    message = user.recv(1024).decode("utf-8")
    print(8)
    if not message:
        root.update()
        print(9)
    else:
        print(10)
        button.config(image=get_next_image())
















