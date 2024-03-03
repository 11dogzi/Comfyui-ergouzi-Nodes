from typing import Tuple, Dict, Any
import torch
from PIL import Image
import numpy as np
from torchvision import transforms


def tensor2pil(image):
    return Image.fromarray(np.clip(255. * image.cpu().numpy().squeeze(), 0, 255).astype(np.uint8))


def pil2tensor(image):
    return torch.from_numpy(np.array(image).astype(np.float32) / 255.0).unsqueeze(0)


class EGTXZZCJNode:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "original_image": ("IMAGE",),
                "original_mask": ("MASK",),  
            },
            "optional": {
                "Up": ("INT", {"default": 0, "min": 0}),
                "Down": ("INT", {"default": 0, "min": 0}),
                "Left": ("INT", {"default": 0, "min": 0}),
                "Right": ("INT", {"default": 0, "min": 0}),
            },
        }

    RETURN_TYPES = ("IMAGE", "MASK", "COORDS")
    RETURN_NAMES = ("cropped_image", "cropped_mask", "Crop_data")
    FUNCTION = "mask_crop"
    CATEGORY = "2🐕/🔍Refinement processing"

    def mask_crop(self, original_image, original_mask, Up=0, Down=0, Left=0, Right=0):
        
        image_pil = tensor2pil(original_image)
        mask_pil = tensor2pil(original_mask)

        
        mask_array = np.array(mask_pil) > 0

        
        coords = np.where(mask_array)
        if coords[0].size == 0 or coords[1].size == 0:
            
            return (original_image, None, original_image)

        x0, y0, x1, y1 = coords[1].min(), coords[0].min(), coords[1].max(), coords[0].max()

        
        x0 -= Left
        y0 -= Up
        x1 += Right
        y1 += Down

        
        x0 = max(x0, 0)
        y0 = max(y0, 0)
        x1 = min(x1, image_pil.width)
        y1 = min(y1, image_pil.height)

        
        cropped_image_pil = image_pil.crop((x0, y0, x1, y1))

        
        cropped_mask_pil = mask_pil.crop((x0, y0, x1, y1))

        
        cropped_image_tensor = pil2tensor(cropped_image_pil)
        cropped_mask_tensor = pil2tensor(cropped_mask_pil)

        
        return (cropped_image_tensor, cropped_mask_tensor, (y0, y1, x0, x1))

NODE_CLASS_MAPPINGS = { "ER_TX_ZZCJ": EGTXZZCJNode }
NODE_DISPLAY_NAME_MAPPINGS = { "ER_TX_ZZCJ": "2🐕Cropping image mask areas" }




