from typing import Tuple, Dict, Any
import torch
from PIL import Image
import numpy as np
from torchvision import transforms


def tensor2pil(image):
    return Image.fromarray(np.clip(255. * image.cpu().numpy().squeeze(), 0, 255).astype(np.uint8))


def pil2tensor(image):
    return torch.from_numpy(np.array(image).astype(np.float32) / 255.0).unsqueeze(0)


class EGJXFZNODE:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image": ("IMAGE",),
                "direction": (["level", "vertical"],),
            },
        }

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("image",)
    FUNCTION = "image_flip"
    CATEGORY = "2🐕/🖼️Image"

    def image_flip(self, image, direction):
        batch_tensor = []
        for image in image:
            image = tensor2pil(image)
            if direction == 'level':
                image = image.transpose(Image.FLIP_LEFT_RIGHT)
            elif direction == 'vertical':
                image = image.transpose(Image.FLIP_TOP_BOTTOM)
            batch_tensor.append(pil2tensor(image))
        batch_tensor = torch.cat(batch_tensor, dim=0)
        return (batch_tensor, )





