from pathlib import Path
from tkinter import *
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox,filedialog
import tkinter as tk
import pyqrcode
import png


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Tushar\Desktop\Qr code generator\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def generate_Qr():
    print("button_1 clicked")
    if len(user_input.get()) !=0:
        global qr,img
        qr=pyqrcode.create(user_input.get())
        img = BitmapImage(data=qr.xbm(scale=5))
    else:
        messagebox.showwarning('warning',"fields are required!")
    try:
        create_download_button()
        display_code()
    except:
        pass

def display_code():
    image_1_lbl.config(image= img)
    print("QR code generated : "+ user_input.get())

def create_download_button():
    download_button = Button(
        image=download_buttonimg,
        borderwidth=0,
        highlightthickness=0,
        relief="flat",
        text="Download QR Code",
        command=download_qr_code
    )
    download_button.place(
        x=237.0,
        y=465.0,
        width=163.0,
        height=51.0
    )

def download_qr_code():
    save_path = tk.filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    if save_path:
        qr.png(save_path, scale=10)
        messagebox.showinfo("Download Successful", f"QR Code saved to {save_path}")
    else:
        messagebox.showwarning("Warning", "Failed!")


def on_entry_click(event):
   if entry_1.get() == "Enter Text":
      entry_1.delete(0, tk.END)
      entry_1.configure(foreground="black")

def on_focus_out(event):
   if entry_1.get() == "":
      entry_1.insert(0, "Enter Text")
      entry_1.configure(foreground="gray")

window = Tk()
window.title("QR Code Generator")
window.geometry("990x600")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 600,
    width = 990,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_text(
    60.0,
    20.0,
    anchor="nw",
    text="Qr generator",
    fill="#000000",
    font=("Bold", 50 * -1)
)

canvas.create_text(
    52.0,
    194.0,
    anchor="nw",
    text="Create Your QR Code\nin Just a Few Clicks",
    fill="#000000",
    font=("Inter SemiBold", 40 * -1)
)

canvas.create_text(
    52.0,
    313.0,
    anchor="nw",
    text="Paste a url or enter text to create a QR code",
    fill="#000000",
    font=("Inter Light", 18 * -1)
)

entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    272.0,
    404.5,
    image=entry_image_1
)

user_input = StringVar()
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    textvariable = user_input,
    highlightthickness=0,
    font=("Inter Light", 15* -1)
)
entry_1.place(
    x=69.0,
    y=373.0,
    width=406.0,
    height=61.0
)

entry_1.insert(0, "Enter Text")
entry_1.bind("<FocusIn>", on_entry_click)
entry_1.bind("<FocusOut>", on_focus_out)

image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    751.0,
    337.0,
    image=image_image_1
)

image_1_lbl =Label(
    window,
    bg='#E0E0E0')

image_1_lbl.place(
    x=620.0,
    y=195.0,
    width=263.0,
    height=285.0
)

generate_buttonimg = PhotoImage(file=relative_to_assets("button_1.png"))
download_buttonimg = PhotoImage(file=relative_to_assets("button_2.png"))
button_1 = Button(
    image=generate_buttonimg,
    borderwidth=0,
    highlightthickness=0,
    relief="flat",
    command = generate_Qr
)
button_1.place(
    x=49.0,
    y=465.0,
    width=163.0,
    height=51.0
)
window.mainloop()
