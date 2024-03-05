import numpy as np
import torch
from PIL import Image, ImageFilter

specific_filters = [
    'BLUR',
    'CONTOUR',
    'DETAIL',
    'EDGE_ENHANCE',
    'EDGE_ENHANCE_MORE',
    'EMBOSS',
    'FIND_EDGES',
    'GaussianBlur',
    'MaxFilter',
    'MedianFilter',
    'MinFilter',
    'ModeFilter',
    'SHARPEN',
    'SMOOTH',
    'SMOOTH_MORE',
    'UnsharpMask'
]


class EGTXLJNode:
    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "apply_filter"
    CATEGORY = "2🐕/🖼️Image/🪞Filter"
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "image": ("IMAGE",),
                "filter_type": (specific_filters,),
            },
        }
    
    def apply_filter(
        self,
        image: torch.Tensor,
        filter_type: str,
    ):
        if filter_type not in specific_filters:
            raise ValueError(f"Unknown filter type: {filter_type}")
    
        image_pil = Image.fromarray((image[0].numpy() * 255).astype(np.uint8))
    
        try:
            filter_instance = getattr(ImageFilter, filter_type)
        except AttributeError:
            filter_method = getattr(image_pil, filter_type)
            if callable(filter_method):
                filter_instance = filter_method()
            else:
                raise ValueError(f"Unknown filter type: {filter_type}")
    
        try:
            image_pil = image_pil.filter(filter_instance)
        except TypeError:
            filter_method = getattr(image_pil, filter_type)
            if callable(filter_method):
                default_params = filter_method.__defaults__
                if default_params:
                    filter_instance = filter_method(*default_params)
                    image_pil = image_pil.filter(filter_instance)
                else:
                    raise TypeError(f"Filter {filter_type} requires arguments but no default parameters are provided.")
            else:
                raise TypeError(f"Unknown filter type: {filter_type}")
    
        image_tensor = torch.from_numpy(np.array(image_pil).astype(np.float32) / 255).unsqueeze(0)
    
        return (image_tensor,)

