import os
import numpy as np
import torch
import sys
from PIL import Image, ImageOps
from torchvision import transforms as T
from torchvision.transforms import functional as TF




my_dir = os.path.dirname(os.path.abspath(__file__))
custom_nodes_dir = os.path.abspath(os.path.join(my_dir, '.'))
comfy_dir = os.path.abspath(os.path.join(my_dir, '..'))
sys.path.append(comfy_dir)

from nodes import MAX_RESOLUTION


def tensor2pil(image: torch.Tensor) -> Image.Image:
    return Image.fromarray(np.clip(255. * image.cpu().numpy().squeeze(), 0, 255).astype(np.uint8))


def pil2tensor(image: Image.Image) -> torch.Tensor:
    return torch.from_numpy(np.array(image).astype(np.float32) / 255.0).unsqueeze(0)

def common_upscale(samples, Scale_width, Scale_height, upscale_method, crop):
        if crop == "center":
            old_Scale_width = samples.shape[3]
            old_Scale_height = samples.shape[2]
            old_aspect = old_Scale_width / old_Scale_height
            new_aspect = Scale_width / Scale_height
            x = 0
            y = 0
            if old_aspect > new_aspect:
                x = round((old_Scale_width - old_Scale_width * (new_aspect / old_aspect)) / 2)
            elif old_aspect < new_aspect:
                y = round((old_Scale_height - old_Scale_height * (old_aspect / new_aspect)) / 2)
            s = samples[:,:,y:old_Scale_height-y,x:old_Scale_width-x]
        else:
            s = samples

        if upscale_method == "bislerp":
            return bislerp(s, Scale_width, Scale_height)
        elif upscale_method == "lanczos":
            return lanczos(s, Scale_width, Scale_height)
        else:
            return torch.nn.functional.interpolate(s, size=(Scale_height, Scale_width), mode=upscale_method)


class EGCPSYTJNode:

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "original_image": ("IMAGE",),
                "Watermark_image": ("IMAGE",),
                "Zoom_mode": (["None", "Fit", "zoom", "Scale_according_to_input_width_and_height"],),
                "Scaling_method": (["nearest-exact", "bilinear", "area"],),
                "Scaling_factor": ("FLOAT", {"default": 1, "min": 0.01, "max": 16.0, "step": 0.1}),
                "Scale_width": ("INT", {"default": 512, "min": 0, "max": MAX_RESOLUTION, "step": 64}),
                "Scale_height": ("INT", {"default": 512, "min": 0, "max": MAX_RESOLUTION, "step": 64}),
                "initial_position": (["Centered", "Up", "Down", "Left", "Right", "Up Left", "Up Right", "Down Left", "Down Right"],),
                "X_direction": ("INT", {"default": 0, "min": -48000, "max": 48000, "step": 10}),
                "Y_direction": ("INT", {"default": 0, "min": -48000, "max": 48000, "step": 10}),
                "rotate": ("INT", {"default": 0, "min": -180, "max": 180, "step": 5}),
                "transparency": ("FLOAT", {"default": 0, "min": 0, "max": 100, "step": 5, "display": "slider"}),
            },
            "optional": {"mask": ("MASK",),}
        }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "apply_Watermark_image"
    CATEGORY = "2🐕/🔖Watermark addition"

    def apply_Watermark_image(self, original_image, Watermark_image, Zoom_mode, Scaling_method, Scaling_factor,
                            Scale_width, Scale_height, X_direction, Y_direction, rotate, transparency, initial_position, mask=None):

        
        size = Scale_width, Scale_height
        location = X_direction, Y_direction
        mask = mask

        
        if Zoom_mode != "None":
            
            Watermark_image_size = Watermark_image.size()
            Watermark_image_size = (Watermark_image_size[2], Watermark_image_size[1])
            if Zoom_mode == "Fit":
                h_ratio = original_image.size()[1] / Watermark_image_size[1]
                w_ratio = original_image.size()[2] / Watermark_image_size[0]
                ratio = min(h_ratio, w_ratio)
                Watermark_image_size = tuple(round(dimension * ratio) for dimension in Watermark_image_size)
            elif Zoom_mode == "zoom":
                Watermark_image_size = tuple(int(dimension * Scaling_factor) for dimension in Watermark_image_size)
            elif Zoom_mode == "Scale_according_to_input_width_and_height":
                Watermark_image_size = (size[0], size[1])

            samples = Watermark_image.movedim(-1, 1)
            Watermark_image =common_upscale(samples, Watermark_image_size[0], Watermark_image_size[1], Scaling_method, False)
            Watermark_image = Watermark_image.movedim(1, -1)
            
        Watermark_image = tensor2pil(Watermark_image)

         
        Watermark_image = Watermark_image.convert('RGBA')
        Watermark_image.putalpha(Image.new("L", Watermark_image.size, 255))

        
        if mask is not None:
            
            mask = tensor2pil(mask)
            mask = mask.resize(Watermark_image.size)
            
            Watermark_image.putalpha(ImageOps.invert(mask))

        
        Watermark_image = Watermark_image.rotate(rotate, expand=True)

        
        r, g, b, a = Watermark_image.split()
        a = a.point(lambda x: max(0, int(x * (1 - transparency / 100))))
        Watermark_image.putalpha(a)
        
        
        print(f"Alignment value received: {initial_position}")
        
        
        print(f"Base Image Size: {original_image.size()}")
        
        print(f"Overlay Image Size: {Watermark_image.size}")
        
        original_image_Scale_width, original_image_Scale_height = original_image.size()[2], original_image.size()[1]
        Watermark_image_Scale_width, Watermark_image_Scale_height = Watermark_image.size
        
        print(f"Original X_direction: {X_direction}, Y_direction: {Y_direction}")
        
        
        X_direction_int = None
        Y_direction_int = None
        
        if initial_position == "Centered":
            X_direction_int = int(X_direction + (original_image_Scale_width - Watermark_image_Scale_width) / 2)
            Y_direction_int = int(Y_direction + (original_image_Scale_height - Watermark_image_Scale_height) / 2)
        elif initial_position == "Up":
            X_direction_int = int(X_direction + (original_image_Scale_width - Watermark_image_Scale_width) / 2)
            Y_direction_int = Y_direction  
        elif initial_position == "Down":
            X_direction_int = int(X_direction + (original_image_Scale_width - Watermark_image_Scale_width) / 2)
            Y_direction_int = int(Y_direction + original_image_Scale_height - Watermark_image_Scale_height)
        elif initial_position == "Left":
            Y_direction_int = int(Y_direction + (original_image_Scale_height - Watermark_image_Scale_height) / 2)
            X_direction_int = X_direction  
        elif initial_position == "Right":
            X_direction_int = int(X_direction + original_image_Scale_width - Watermark_image_Scale_width)
            Y_direction_int = int(Y_direction + (original_image_Scale_height - Watermark_image_Scale_height) / 2)
        elif initial_position == "Up Left":
            pass  
        elif initial_position == "Up Right":
            X_direction_int = int(original_image_Scale_width - Watermark_image_Scale_width + X_direction)  
            Y_direction_int = Y_direction  
        elif initial_position == "Down Left":
            X_direction_int = X_direction  
            Y_direction_int = int(original_image_Scale_height - Watermark_image_Scale_height + Y_direction) 
        elif initial_position == "Down Right":
            X_direction_int = int(X_direction + original_image_Scale_width - Watermark_image_Scale_width)
            Y_direction_int = int(Y_direction + original_image_Scale_height - Watermark_image_Scale_height)
        
        if X_direction_int is not None and Y_direction_int is not None:
            
            location = X_direction_int, Y_direction_int
        else:
            
            location = X_direction, Y_direction

        
        original_image_list = torch.unbind(original_image, dim=0)

        
        processed_original_image_list = []
        for tensor in original_image_list:
            
            image = tensor2pil(tensor)

            
            if mask is None:
                image.paste(Watermark_image, location)
            else:
                image.paste(Watermark_image, location, Watermark_image)

            
            processed_tensor = pil2tensor(image)

            
            processed_original_image_list.append(processed_tensor)

        
        original_image = torch.stack([tensor.squeeze() for tensor in processed_original_image_list])

        
        return (original_image,)
NODE_CLASS_MAPPINGS = { "EG_CPSYTJ": EGCPSYTJNode }
NODE_DISPLAY_NAME_MAPPINGS = { "EG_CPSYTJ": "2🐕Add finished watermark image" }
