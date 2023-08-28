import qrcode
from tkinter import *
from tkinter import messagebox

win = Tk()
win.title("Joe's QR Code Generator")
win.resizable(False, False)  # This code helps to disable windows from resizing

window_height = 500
window_width = 900

screen_width = win.winfo_screenwidth()
screen_height = win.winfo_screenheight()

x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))

win.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

win.config(bg='SteelBlue3')


def generateCode():
    # Creating a QRCode object of the size specified by the user
    qr = qrcode.QRCode(version=size.get(),
                       box_size=10,
                       border=5)
    qr.add_data(text.get())  # Adding the data to be encoded to the QRCode object
    qr.make(fit=True)  # Making the entire QR Code space utilized
    img = qr.make_image()  # Generating the QR Code
    file_direc = loc.get() + '\\' + name.get()  # Getting the directory where the file has to be save
    img.save(f'{file_direc}.png')  # Saving the QR Code
    # Showing the pop up message on saving the file
    messagebox.showinfo("QR Code Generator", "QR Code is saved successfully!")


# Label for the window
heading_frame = Frame(win, bg="azure", bd=5)
heading_frame.place(relx=0.15, rely=0.05, relwidth=0.7, relheight=0.1)
heading_label = Label(heading_frame, text="Generate QR Code", bg='azure', font=('Times', 20, 'bold'))
heading_label.place(relx=0, rely=0, relwidth=1, relheight=1)

# Taking the input of the text or URL to get QR code
frame1 = Frame(win, bg="SteelBlue3")
frame1.place(relx=0.1, rely=0.15, relwidth=0.7, relheight=0.3)
label1 = Label(frame1, text="Enter the text/URL: ", bg="SteelBlue3", fg='azure', font=('Courier', 13, 'bold'))
label1.place(relx=0.05, rely=0.2, relheight=0.08)
text = Entry(frame1, font='Century 12')
text.place(relx=0.05, rely=0.4, relwidth=1, relheight=0.2)
text.insert(END, "https://precisionresource.sharepoint.com/teams/PRBPublic/SitePages/??.aspx")

# Getting input of the location to save QR Code
frame2 = Frame(win, bg="SteelBlue3")
frame2.place(relx=0.1, rely=0.35, relwidth=0.7, relheight=0.3)
label2 = Label(frame2, text="Enter the location to save the QR Code: ", bg="SteelBlue3", fg='azure',
               font=('Courier', 13, 'bold'))
label2.place(relx=0.05, rely=0.2, relheight=0.08)
loc = Entry(frame2, font='Century 12')
loc.place(relx=0.05, rely=0.4, relwidth=1, relheight=0.2)
loc.insert(END, 'C:\\data\\')

# Getting input of the QR Code image name
frame3 = Frame(win, bg="SteelBlue3")
frame3.place(relx=0.1, rely=0.55, relwidth=0.7, relheight=0.3)
label3 = Label(frame3, text="Enter the name of the QR Code: ", bg="SteelBlue3", fg='azure',
               font=('Courier', 13, 'bold'))
label3.place(relx=0.05, rely=0.2, relheight=0.08)
name = Entry(frame3, font='Century 12')
name.place(relx=0.05, rely=0.4, relwidth=1, relheight=0.2)
# Getting the input of the size of the QR Code
frame4 = Frame(win, bg="SteelBlue3")
frame4.place(relx=0.1, rely=0.75, relwidth=0.7, relheight=0.2)
label4 = Label(frame4, text="Enter the size from 1 to 40 with 1 being 21x21: ", bg="SteelBlue3", fg='azure',
               font=('Courier', 13, 'bold'))
print(label4)
label4.place(relx=0.05, rely=0.2, relheight=0.08)
size = Entry(frame4, font='Century 12')
size.insert(END, "10")

size.place(relx=0.05, rely=0.4, relwidth=0.5, relheight=0.2)

# Button to generate and save the QR Code
button = Button(win, text='Generate Code', font=('Courier', 15, 'normal'), command=generateCode)
button.place(relx=0.35, rely=0.9, relwidth=0.25, relheight=0.05)
# Runs the window till it is closed manually
win.mainloop()

if __name__ == '__main__':
    pass
