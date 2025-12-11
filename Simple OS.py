import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk, ImageDraw
import pygame


def login():
    def logging():
        pin_num = str(pin.get())

        if pin_num == '12345':
            login_windows.destroy()
            pygame.mixer.init()
            pygame.mixer.music.load('startup.mp3')
            pygame.mixer.music.play()
            main_windows()
        else:
            messagebox.showinfo("Error", "Invalid PIN")

    login_windows = tk.Tk()
    login_windows.geometry('1000x500')
    login_windows.title('Login')
    login_windows.config(background="black")
    login_windows.title("Login")
    login_windows.resizable(False, False)

    image_path = "pfp.jpg"
    original_image = Image.open(image_path).resize((200, 200), Image.LANCZOS)
    mask = Image.new("L", original_image.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, original_image.size[0], original_image.size[1]), fill=255)
    rounded_image = Image.new("RGBA", original_image.size)
    rounded_image.paste(original_image, (0, 0), mask=mask)
    tk_image = ImageTk.PhotoImage(rounded_image)
    label = tk.Label(login_windows, image=tk_image)
    label.pack()

    pin_number = tk.Label(login_windows, text="Enter Pin", fg="white", bg="Black")
    pin_number.pack()
    pin = tk.Entry(login_windows, width=10)
    pin.config(font="Arial", bg="White")
    pin.pack(pady=5)

    login_button = tk.Button(login_windows, text="Login", command=logging)
    login_button.pack()

    login_windows.mainloop()


def main_windows():
    main_windows = tk.Tk()
    main_windows.attributes("-fullscreen", True)
    main_windows.title('Main Window')
    main_windows.config(background="black")

    taskbar_frame = tk.Frame(main_windows, bg="lightgray", height=50)
    taskbar_frame.pack(side=tk.BOTTOM, fill=tk.X)

    button1 = tk.Button(taskbar_frame, text="BlueMoon")
    button1.pack(side=tk.LEFT, padx=5, pady=5)

    button2 = tk.Button(taskbar_frame, text="App 2")
    button2.pack(side=tk.LEFT, padx=5, pady=5)
    main_windows.mainloop()


if __name__ == '__main__':
   login()
