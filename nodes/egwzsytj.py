import numpy as np
import torch
import os
from PIL import Image, ImageDraw, ImageOps, ImageFont

colour_mapping = {
    "White": (255, 255, 255),
    "Black": (0, 0, 0),
    "Red": (255, 0, 0),
    "Green": (0, 255, 0),
    "Blue": (0, 0, 255),
    "Yellow": (255, 255, 0),
    "Light_blue": (0, 255, 255),
    "magenta": (255, 0, 255),
    "orange": (255, 165, 0),
    "purple": (128, 0, 128),
    "pink": (255, 192, 203),
    "brown": (160, 85, 15),
    "gray": (128, 128, 128),
    "Light_Grey": (211, 211, 211),
    "Dark_Grey": (102, 102, 102),
    "Olive_Green": (128, 128, 0),
    "Acid_Orange": (0, 128, 0),
    "Duck_Green": (0, 128, 128),
    "Navy_Blue": (0, 0, 128),
    "Purple_Brown": (128, 0, 0),
    "Purple_red": (255, 0, 128),
    "light_green": (0, 255, 128),
    "silver": (192, 192, 192),
    "gold": (255, 215, 0),
    "turquoise": (64, 224, 208),
    "light_purple": (230, 230, 250),
    "Blue_Purple": (238, 130, 238),
    "Coral_Red": (255, 127, 80),
    "Indigo_Blue": (75, 0, 130),    
}

COLORS = ["custom", "White", "Black", "Red", "Green", "Blue", "Yellow",
          "Light_blue", "magenta", "orange", "purple", "pink", "brown", "gray",
          "Light_Grey", "Dark_Grey", "Olive_Green", "Acid_Orange", "Duck_Green", "Navy_Blue", "Purple_Brown",
          "Purple_red", "light_green", "silver", "gold", "turquoise", "light_purple",
          "Blue_Purple", "Coral_Red", "Indigo_Blue"]

ALIGN_OPTIONS = ["Centered", "Up", "Down"]                 
ROTATE_OPTIONS = ["Center_by_Text", "Center_by_Image"]
JUSTIFY_OPTIONS = ["Centered", "Left", "Right"]
PERSPECTIVE_OPTIONS = ["Up", "Down", "Left", "Right"]

def Vertical_position_text(Vertical_position, img_height, text_height, text_pos_y, margins):
    if Vertical_position == "Centered":
        text_plot_y = img_height / 2 - text_height / 2 + text_pos_y
    elif Vertical_position == "Up":
        text_plot_y = 0 + text_pos_y
    elif Vertical_position == "Down":
        text_plot_y = img_height - text_height + text_pos_y
    return text_plot_y

def get_text_size(draw, text, font):
    bbox = draw.textbbox((0, 0), text, font=font)

    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    return text_width, text_height

def Horizontal_position_text(Horizontal_position, img_width, line_width, margins):
    if Horizontal_position == "Left":
        text_plot_x = 0 + margins
    elif Horizontal_position == "Right":
        text_plot_x = img_width - line_width - margins
    elif Horizontal_position == "Centered":
        text_plot_x = img_width/2 - line_width/2 + margins
    return text_plot_x

def Hexadecimal_to_rgb(Hexadecimal_colour):
    Hexadecimal_colour = Hexadecimal_colour.lstrip('#')  # Remove the '#' character, if present
    r = int(Hexadecimal_colour[0:2], 16)
    g = int(Hexadecimal_colour[2:4], 16)
    b = int(Hexadecimal_colour[4:6], 16)
    return (r, g, b)

def get_colour_values(colour, colour_Hexadecimal, colour_mapping):
    
    if colour == "custom":
        colour_rgb = Hexadecimal_to_rgb(colour_Hexadecimal)
    else:
        colour_rgb = colour_mapping.get(colour, (0, 0, 0))  # Default to Black if the colour is not found
    return colour_rgb

def tensor2pil(image):
    return Image.fromarray(np.clip(255. * image.cpu().numpy().squeeze(), 0, 255).astype(np.uint8)) 

def pil2tensor(image):
    return torch.from_numpy(np.array(image).astype(np.float32) / 255.0).unsqueeze(0) 

def draw_masked_text(text_mask, text,
                     font_name, font_size, font_opacity,
                     margins, Row_spacing,
                     X_offset, Y_offset,
                     Vertical_position, Horizontal_position,
                     rotation_angle, rotation_options):
    
    text_mask = Image.new('RGBA', text_mask.size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(text_mask)
    
    font_folder = "fonts"
    font_file = os.path.join(font_folder, font_name)
    resolved_font_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), font_file)
    font = ImageFont.truetype(resolved_font_path, size=font_size)
    
    image_width = text_mask.size[0]
    
    image_height = text_mask.size[1]
    
    text_lines = text.split('\n')
    
    max_text_width = 0
    max_text_height = 0
    for line in text_lines:
        w, h = draw.textsize(line, font=font)
        max_text_width = max(max_text_width, w)
        max_text_height = max(max_text_height, h + Row_spacing)
    
    text_x = X_offset
    text_y = Y_offset
    
    text_plot_y = Vertical_position_text(Vertical_position, image_height, max_text_height * len(text_lines), text_y, margins)
    text_plot_x = Horizontal_position_text(Horizontal_position, image_width, max_text_width, margins) + text_x
    
    for line in text_lines:
        w, h = draw.textsize(line, font=font)
        current_y = text_plot_y
        draw.text((text_plot_x, current_y), line, font=font, fill=(255, 255, 255, font_opacity))
        text_plot_y += h + Row_spacing
    
    if rotation_angle != 0:
        if rotation_options == "Center_by_Text":
            rotated_text_mask = text_mask.rotate(rotation_angle, center=(text_x + max_text_width / 2, text_y / 2))
        elif rotation_options == "Center_by_Image":    
            rotated_text_mask = text_mask.rotate(rotation_angle, center=(image_width / 2, image_height / 2))
    else:
        rotated_text_mask = text_mask
    
    return rotated_text_mask

class EGYSZTNode:
    @classmethod
    def INPUT_TYPES(s):
        font_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "fonts")
        file_list = [f for f in os.listdir(font_dir) if os.path.isfile(os.path.join(font_dir, f)) and f.lower().endswith(".ttf")]
        
        return {"required": {
                    "width": ("INT", {"default": 512, "min": 64, "max": 20000}),
                    "height": ("INT", {"default": 512, "min": 64, "max": 20000}),
                    "text": ("STRING", {"multiline": True, "default": "Please enter the watermark text that needs to be generated. The fonts in this plugin are all publicly available online resources and are for learning and communication purposes only. If you need a commercial font, please replace it yourself. The font storage path is in the Comfyui ergouzi DGNJD \ fonts folder. For more SD tutorials, please refer to theB站@灵仙儿和二狗子🐕"}),
                    "Font": (file_list,),
                    "Font_size": ("INT", {"default": 50, "min": 1, "max": 1024}),
                    "Font_color": (COLORS,),
                    "Background_color": (COLORS,),
                    "Vertical_position": (ALIGN_OPTIONS,),
                    "Horizontal_position": (JUSTIFY_OPTIONS,),
                    "Text_margin": ("INT", {"default": 0, "min": -1024, "max": 1024}),
                    "Row_spacing": ("INT", {"default": 0, "min": -1024, "max": 1024}),
                    "X_offset": ("INT", {"default": 0, "min": -20000, "max": 20000}),
                    "Y_offset": ("INT", {"default": 0, "min": -20000, "max": 20000}),
                    "Rotate": ("FLOAT", {"default": 0.0, "min": -360.0, "max": 360.0, "step": 0.1}),
                    "Rotation_center": (ROTATE_OPTIONS,),
                    "Font_transparency": ("INT", {
                        "default": 255, 
                        "min": 0, 
                        "max": 255, 
                        "display": "slider"
                     }),
                },
                "optional": {
                    "Font_colour_Hexadecimal": ("STRING", {"multiline": False, "default": "#000000"}),
                    "Background_colour_Hexadecimal": ("STRING", {"multiline": False, "default": "#000000"}),
                    "image": ("IMAGE", {}),
                }
        }
    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("Output_Image",)
    FUNCTION = "draw_text"
    CATEGORY = "2🐕/🔖Watermark addition"
    def draw_text(self, width, height, text,
                  Font, Font_size, Font_color,
                  Background_color,
                  Text_margin, Row_spacing,
                  X_offset, Y_offset,
                  Vertical_position, Horizontal_position,
                  Rotate, Rotation_center,
                  Font_colour_Hexadecimal='#000000', Background_colour_Hexadecimal='#000000', image=None,
                  Font_transparency=255):
        font_opacity = Font_transparency
        text_colour = get_colour_values(Font_color, Font_colour_Hexadecimal, colour_mapping)
        bg_colour = get_colour_values(Background_color, Background_colour_Hexadecimal, colour_mapping)
        if image is not None:
            back_image = tensor2pil(image)  # Assuming tensor2pil converts a tensor to PIL Image
            size = back_image.size
        else:
            size = (width, height)
            back_image = Image.new('RGB', size, bg_colour)
        text_image = Image.new('RGB', size, text_colour)
        text_mask = Image.new('L', back_image.size)
        rotated_text_mask = draw_masked_text(text_mask, text, Font, Font_size, font_opacity,
                                             Text_margin, Row_spacing,
                                             X_offset, Y_offset,
                                             Vertical_position, Horizontal_position,
                                             Rotate, Rotation_center)
        image_out = Image.composite(text_image, back_image, rotated_text_mask)
        return (pil2tensor(image_out),)
NODE_CLASS_MAPPINGS = { "EG-YSZT-ZT" : EGYSZTNode }
NODE_DISPLAY_NAME_MAPPINGS = { "EG-YSZT-ZT" : "2🐕Text watermark addition" }


