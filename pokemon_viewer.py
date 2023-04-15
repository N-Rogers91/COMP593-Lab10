from tkinter import *
from tkinter import ttk
import os
import ctypes
import pokeapi

# Get the path of the script and its parent directory
script_path = os.path.abspath(__file__)
script_dir = os.path.dirname(script_path)

#Create image cache directory
image_cache_dir = os.path.join(script_dir, 'images')
if not os.path.isdir(image_cache_dir):
    os.makedirs(image_cache_dir)


# Create the main window
root = Tk()
root.title("Pokemon image viewer")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.minsize(500, 600)

# Set the window icon
icon_path = os.path.join(script_dir, 'Poke-Ball.ico')
app_id = 'COMP593.PokeImageViewer'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(app_id)
root.iconbitmap(icon_path)

#put fram on the GUI
frame = ttk.Frame(root)
frame.grid(row=0, column=0, sticky=NSEW)
frame.rowconfigure(0, weight=100)

#put image into frame
image_path = os.path.join(script_dir, 'logo.png')
img_poke = PhotoImage(file=image_path)
lbl_image = ttk.Label(frame, image=img_poke)
lbl_image.grid(padx=10, pady=10)

#put pulldown list of pokemon frame

pokemon_name_list = sorted(pokeapi.get_pokemon_names())
cbox_pokemon_names = ttk.Combobox(frame, values=pokemon_name_list, state='readonly')
cbox_pokemon_names.set("Select a Pokemon")
cbox_pokemon_names.grid(padx=10, pady=10)

def handle_pokemon_sel(event):
    #os_logo = ('WindowsLogo.png', 'MacOSLogo.png', 'LinuxLogo.png')
    sel_pokemon = cbox_pokemon_names.get()
    global image_path
    image_path = pokeapi.download_pokemon_artwork(sel_pokemon, image_cache_dir)
    img_poke['file'] = image_path
    return

cbox_pokemon_names.bind('<<ComboboxSelected>>', handle_pokemon_sel)

def handle_set_desktop():
    image_lib.set_desktop_background_image(image_path)


#"Set desktop" button frame
btn_set_desktop = ttk.Button(frame, text='Set as desktop image', command=handle_set_desktop)
btn_set_desktop.grid(padx=10, pady=10)
                                                            



# TODO: Put code here
root.mainloop()
