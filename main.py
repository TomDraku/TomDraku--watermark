from tkinter import*
from tkinter.ttk import *
from tkinter import filedialog
from PIL import ImageTk, Image, ImageDraw, ImageFont



myimage = None

# opening photo for adding watermark
def open():
    global myimage
    root.filename = filedialog.askopenfilename(initialdir="C:/Users/t_zac/Pictures", title="Search for photo", filetypes=( ("jpg files", "*.jpg"),("png files", "*.png"), ("jpeg files", "*.jpeg")))
    try:
        myimage = (Image.open(root.filename))
    except AttributeError:
        print("Something is wrong with the image file" ) 
    
   
    
# ADDING TEXT TO IMAGE

def add_text():
    picture_size = myimage.size
    width = picture_size[0]
    height = picture_size[1]
    # call the draw function to add 2 graphic to image
    I1 = ImageDraw.Draw(myimage)
    # costume font style and font size
    myFont = ImageFont.truetype('arial', int(height*0.03))
    text = gettext()
    text_size = myFont.getsize(text)
    text_width = text_size[0]
    text_height = text_size[1]
    # add text to the image
    I1.text((width-text_width*1.5, height-text_height*2),text, font=myFont, fill=(255,255,255))
    # display the image
    myimage.show()
    open_popup()
    
def add_stamp():
    picture_size = myimage.size
    width = picture_size[0]
    height = picture_size[1]

    # watermark image
    imWater = Image.open("Wphoto.jpg")
    size = (int(width*0.1), int(height*0.1))
    imWater.thumbnail(size)
    
    width_imWater = imWater.size[0]
    height_imWather = imWater.size[1]
    myimage.paste(imWater, (int(width-width_imWater-0.03*width), int(height-height_imWather-0.03*height)))
    myimage.show()
    open_popup()
    


    
# getting text for adding as a watermark
def gettext():
    text = e.get()
    return text

# saving image to file
def save_image():
    myimage.save("C:/Users/t_zac/Pictures/modified.jpg")
    top.destroy()

# asking for acceptation of the watermark
def open_popup():
    global top
    top= Toplevel(root)
    top.geometry("350x150")
    top.title("Acceptation")
    Label(top, text="Do you want to save the photo?").place(x=90,y=20)
    # create button for adding photo
    yes_button = Button(top, text="Yes", command=save_image).place(x=90,y=70)
    no_button = Button(top, text="No", command=top.destroy).place(x=200,y=70)

    
root = Tk()

# specify size of the window
root.geometry("500x340")

# create label
l= Label(root, text="App for doing watermarks")
l.config(font=("Courier",12))

# gird methode for label
l.grid(row=0,column=1, padx=20,pady=10)

# create button for adding photo
add_button = Button(root, text="Find photo", command=open)


# grid methode for button
add_button.grid(row=1, column=0,padx=20, pady=40)

# create text entry
e = Entry(root, text="")


# create button for getting text 
text_button = Button(root, text="Add text", command=lambda:add_text())
 
# grid methode for text button
text_button.grid(row=2, column=0)

# grid methode for text entry
e.grid(row=2, column=1)

# create button for adding watermark image
add_watermark = Button(root, text="Stamp", command=add_stamp)

# grid methode for add_watermark
add_watermark.grid(row=3, column=0,padx=20,pady=40)



mainloop()