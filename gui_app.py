import tkinter as tk
import time
from PIL import Image , ImageTk

#main window
root=tk.Tk()
root.title("Photo Slideshow Album")
root.geometry("900x900")

#list of image paths
Image_paths= [
    r"C:\Users\Samrin\Pictures\Screenshots\img1.png",
    r"C:\Users\Samrin\Pictures\Screenshots\img2.png",
    r"C:\Users\Samrin\Pictures\Screenshots\imgimp.png",
    r"C:\Users\Samrin\Pictures\Screenshots\img5.png",
    r"C:\Users\Samrin\Pictures\Screenshots\img4.png"]
image_size=(400,400)
images=[]
for path in Image_paths:
    img=Image.open(path)
    img=img.resize(image_size)
    images.append(img)  #adding each image int the list

#convert PIL Images into Tkinter Compatible Immage
final_images=[]
for img in images:
    photo=ImageTk.PhotoImage(img) 
    final_images.append(photo)

#label widget to keep photo
image_label=tk.Label(root)
image_label.pack(pady=30)
#slideshow Function
def start_slideshow():
    for photo in final_images:
        image_label.config(image=photo)
        image_label.image=photo
        root.update()
        time.sleep(2)
#button 
play_button=tk.Button(
    root,
    text="Play the Slideshow ",
    font=("Arial",17),
    command=start_slideshow
)
play_button.pack(pady=40)
root.mainloop()