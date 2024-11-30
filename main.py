import pygame
from tkinter import *
from tkinter import messagebox
import json


# Initialize pygame mixer
pygame.mixer.init()


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        # Play the first sound when clicking "Add"
        pygame.mixer.music.load("click_sound.mp3")
        pygame.mixer.music.play()

        is_ok = messagebox.askokcancel(
            title=website,
            message=f"These are the details entered: \nEmail: {email} \nPassword: {password} \nIs it ok to save?"
        )

        # If user clicks "OK", play the finish sound
        if is_ok:
            pygame.mixer.music.load("finish.mp3")
            pygame.mixer.music.play()

            # Save the password data if confirmed
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)

            # Clear input fields
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- Find Password ------------------------------- #
def find_password():
    website = website_entry.get()
    with open("data.json") as data_file:
        data = json.load(data_file)
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Set icon for title bar
logo_img = PhotoImage(file="logo.png")
window.iconphoto(False, logo_img)

# Canvas for logo
canvas = Canvas(height=200, width=200)
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "example@gmail.com")
password_entry = Entry(width=35)
password_entry.grid(row=3, column=1, columnspan=2)

# Buttons
search_button = Button(text="Search", command=find_password)
search_button.grid(row=1, column=3,)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()
