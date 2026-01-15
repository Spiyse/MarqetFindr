import customtkinter as ctk
from pathlib import Path
from tkinter import PhotoImage
from marqet_findr.core import fetch_page, parse_listings
from marqet_findr.config import load_config
from .widgets import TopBar




# Load configuration
config = load_config()

# Build URL from config
base_url = config.get('base_url')
category = config.get('category') # For now the default catagory is pc's
url = base_url + category

# Fetch the page
soup = fetch_page(url, config)


# Parse listings
listings = parse_listings(soup, config)

if not listings:
    print("No listings found")
    exit(1)

# Display a sample listing for now in the terminal so i can see if the listing info is right
if len(listings) > 1:
    sample = listings[1]
    print(f"Name: {sample.get('name')}")
    print(f"Price: {sample.get('price')}")
    print(f"Region: {sample.get('region')}")
    print(f"Image: {sample.get('image')}")
    print(f"Link: https://ss.com{sample.get('link')}")
    
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        base_dir = Path(__file__).resolve().parents[2]
        icon_path = base_dir / "assets" / "MarqetFinder_Logo.png"
        self.icon_image = PhotoImage(file=icon_path)
        
        
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        
        
        self.iconphoto(True, self.icon_image)
        self.title("Marqet Finder")
        self.geometry("1480x940")
        self.minsize(500,350)
        
        if self.tk.call("tk", "windowingsystem") == "win32":
            self.iconbitmap(icon_path.with_suffix(".ico"))
        
        
        # if len(listings) > 1:
        #     sample = listings[2]
        #     label = ctk.CTkLabel(self, text=f"{sample.get('name')}", fg_color="gray", corner_radius=8, width=80, height=40)
        #     label.pack(pady=40)
        #     print(f"Price: {sample.get('price')}")
        #     print(f"Region: {sample.get('region')}")
        #     print(f"Image: {sample.get('image')}")
        #     print(f"Link: https://ss.com{sample.get('link')}")
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)
        self.grid_rowconfigure(2, weight=1)

        self.top = TopBar(self, on_toggle_theme=self.toggle_theme)
        self.top.grid(row=0, column=0, columnspan=2, sticky="ew", padx=12, pady=12)

        

    def toggle_theme(self):
        mode = ctk.get_appearance_mode()
        new_mode = "light" if mode == "Dark" else "dark"
        ctk.set_appearance_mode(new_mode)

        # Update the sun/moon image on the theme button
        if hasattr(self, "top"):
            self.top.update_icon(new_mode)



def run():
    app = App()
    app.mainloop()