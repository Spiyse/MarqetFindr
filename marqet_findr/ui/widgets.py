import customtkinter as ctk
from dataclasses import dataclass
from PIL import Image

@dataclass
class SearchParams:
    query: str
    category: str
    min_price: str
    max_price: str
    
class LabeledEntry(ctk.CTkFrame):
    def __init__(self, master, label: str, placeholder: str = "", **kwargs):
        super().__init__(master, fg_color="transparent", **kwargs)

        self.label = ctk.CTkLabel(self, text=label)
        self.label.pack(anchor="w")

        self.entry = ctk.CTkEntry(self, placeholder_text=placeholder)
        self.entry.pack(fill="x", pady=(4, 0))

    def get(self) -> str:
        return self.entry.get().strip()

    def set(self, value: str):
        self.entry.delete(0, "end")
        self.entry.insert(0, value)


class TopBar(ctk.CTkFrame):
    def __init__(self, master, on_toggle_theme=None, **kwargs):
        super().__init__(master, corner_radius=12, **kwargs)

        self.grid_columnconfigure(0, weight=1)

        # Logo
        logo = Image.open('assets/MarqetFinder_Logo.png')
        self.logo = ctk.CTkImage(light_image=logo, size=(75, 75))

        # Base theme button background
        base_btn_img = Image.open('assets/Theme_Button.png').convert("RGBA")
        bw, bh = base_btn_img.size

        # Sun/moon icons (composited into the center of the base button)
        sun_img = Image.open('assets/Sun.png').convert("RGBA")
        moon_img = Image.open('assets/Moon.png').convert("RGBA")

        icon_size = int(min(bw, bh) * 0.6)
        sun_resized = sun_img.resize((icon_size, icon_size))
        moon_resized = moon_img.resize((icon_size, icon_size))
        

        offset_x = (bw - icon_size) // 2
        offset_y = (bh - icon_size) // 2

        sun_button_img = base_btn_img.copy()
        sun_button_img.paste(sun_resized, (offset_x, offset_y), mask=sun_resized)

        moon_button_img = base_btn_img.copy()
        moon_button_img.paste(moon_resized, (offset_x, offset_y), mask=moon_resized)

        # CTkImage versions scaled to the button size
        self.theme_light = ctk.CTkImage(
            light_image=sun_button_img,
            dark_image=sun_button_img,
            size=(30, 30),
        )
        
        self.theme_dark = ctk.CTkImage(
            light_image=moon_button_img,
            dark_image=moon_button_img,
            size=(30, 30),
        )

        self.title_lbl = ctk.CTkLabel(self, text="", image=self.logo)
        self.title_lbl.grid(row=0, column=0, sticky="w", padx=12, pady=12)


        # Determine initial image based on current appearance mode
        current_mode = ctk.get_appearance_mode()
        initial_image = self.theme_dark if str(current_mode).lower() == "dark" else self.theme_light

        self.theme_btn = ctk.CTkButton(
            self,
            text="",
            image=initial_image,
            width=30,
            height=30,
            fg_color="transparent",
            border_width=0,
            corner_radius=0,
            hover=False,
            command=on_toggle_theme
            
        )
        self.theme_btn.grid(row=0, column=1, sticky="e", padx=12, pady=12)

    def update_icon(self, mode: str = None):
        if mode is None:
            mode = ctk.get_appearance_mode()

        mode_lower = str(mode).lower()

        if mode_lower == "dark":
            self.theme_btn.configure(image=self.theme_dark)
        else:
            self.theme_btn.configure(image=self.theme_light)
        

