import torch
from PIL import Image
import numpy as np
def tensor2pil(image):
    return Image.fromarray(np.clip(255. * image.cpu().numpy().squeeze(), 0, 255).astype(np.uint8))
def pil2tensor(image):
    return torch.from_numpy(np.array(image).astype(np.float32) / 255.0).unsqueeze(0)
def resize_mask(mask_pil, target_size):
    return mask_pil.resize(target_size, Image.LANCZOS)
def image2mask(image_pil):
    # Convert image to grayscale
    image_pil = image_pil.convert("L")
    # Convert grayscale image to binary mask
    threshold = 128
    mask_array = np.array(image_pil) > threshold
    return Image.fromarray((mask_array * 255).astype(np.uint8))
class EGZZHBCJNode:
    def __init__(self):
        pass
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "operation": (["merge", "crop", "intersect", "not_intersect"], {}),
            },
            "optional": {
                "target_image": ("IMAGE", {}),
                "target_mask": ("MASK", {}),
                "source_image": ("IMAGE", {}),
                "source_mask": ("MASK", {}),
            },
        }
    RETURN_TYPES = ("MASK", "IMAGE")
    RETURN_NAMES = ("result_mask", "result_image")
    FUNCTION = "mask_operation"
    CATEGORY = "2🐕/⛱️Mask"
    def mask_operation(self, operation, source_image=None, target_image=None, source_mask=None, target_mask=None):
        # Convert source and target images to masks if provided
        if source_image is not None:
            source_mask_pil = tensor2pil(source_image)
            source_mask_pil = image2mask(source_mask_pil)
        else:
            source_mask_pil = tensor2pil(source_mask)
        if target_image is not None:
            target_mask_pil = tensor2pil(target_image)
            target_mask_pil = image2mask(target_mask_pil)
        else:
            target_mask_pil = tensor2pil(target_mask)
        # Resize source mask to target mask size
        source_mask_pil = resize_mask(source_mask_pil, target_mask_pil.size)
        source_mask_array = np.array(source_mask_pil) > 0
        target_mask_array = np.array(target_mask_pil) > 0
        if operation == "merge":
            result_mask_array = np.logical_or(source_mask_array, target_mask_array)
        elif operation == "crop":
            result_mask_array = np.logical_and(target_mask_array, np.logical_not(source_mask_array))
        elif operation == "intersect":
            result_mask_array = np.logical_and(source_mask_array, target_mask_array)
        elif operation == "not_intersect":
            result_mask_array = np.logical_xor(source_mask_array, target_mask_array)
        else:
            raise ValueError("Invalid operation selected")
        result_mask = Image.fromarray((result_mask_array * 255).astype(np.uint8))
        result_mask_tensor = pil2tensor(result_mask)
        result_image_tensor = pil2tensor(result_mask)
        return [result_mask_tensor, result_image_tensor]
NODE_CLASS_MAPPINGS = { "EG_ZZHBCJ" : EGZZHBCJNode }
NODE_DISPLAY_NAME_MAPPINGS = { "EG_ZZHBCJ" : "2🐕Mask can be cut arbitrarily" }
