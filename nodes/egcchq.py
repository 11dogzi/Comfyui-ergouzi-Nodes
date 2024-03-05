import torch
from typing import Tuple

class EGTXCCHQ:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image_in": ("IMAGE", {}), 
            }
        }

    RETURN_TYPES = ("INT", "INT")
    RETURN_NAMES = ("width", "height") 
    FUNCTION = "get_image_size"
    CATEGORY = "2🐕/🖼️Image" 

    def get_image_size(self, image_in: torch.Tensor) -> Tuple[int, int]:
        if len(image_in.shape) == 4:
            height, width = image_in.shape[1], image_in.shape[2]
        else:
            height, width = image_in.shape[-2], image_in.shape[-1]
        return (width, height)

