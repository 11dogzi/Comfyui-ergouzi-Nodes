from typing import Tuple, Dict, Any
import torch
from PIL import Image
import numpy as np
from torchvision import transforms

def tensor2pil(image):
    return Image.fromarray(np.clip(255. * image.cpu().numpy().squeeze(), 0, 255).astype(np.uint8))

def pil2tensor(image):
    return torch.from_numpy(np.array(image).astype(np.float32) / 255.0).unsqueeze(0)

class EGCJPJNode:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "original_image": ("IMAGE",),
                "cropped_image": ("IMAGE",),
                "Crop_data": ("COORDS",),
            },
        }

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("image",)
    FUNCTION = "resize_and_paste"
    CATEGORY = "2🐕/🔍Refinement processing"

    def resize_and_paste(self, original_image, cropped_image, Crop_data):
        original_image_pil = tensor2pil(original_image)
        cropped_image_pil = tensor2pil(cropped_image)

        if Crop_data is None:
            return (original_image,)

        
        y0, y1, x0, x1 = Crop_data

        target_width = x1 - x0
        target_height = y1 - y0

        cropped_image_pil = cropped_image_pil.resize((target_width, target_height))

        original_image_pil.paste(cropped_image_pil, (x0, y0))

        pasted_image_tensor = pil2tensor(original_image_pil)

        return (pasted_image_tensor,)

NODE_CLASS_MAPPINGS = { "EG_TX_CJPJ": EGCJPJNode }
NODE_DISPLAY_NAME_MAPPINGS = { "EG_TX_CJPJ": "2🐕Image cropping data stitching" }