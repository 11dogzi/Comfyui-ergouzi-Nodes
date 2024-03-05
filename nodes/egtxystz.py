import cv2
import numpy as np
import torch
from PIL import Image, ImageEnhance
class EGHTYSTZNode:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "image": ("IMAGE",),
                "temperature": ("FLOAT", {
                    "default": 0, 
                    "min": -100, 
                    "max": 100, 
                    "step": 100,
                    "precision": 5,
                    "display": "slider" 
                }),
                "hue": ("FLOAT", {
                    "default": 0, 
                    "min": -90, 
                    "max": 90, 
                    "step": 5,
                    "precision": 180,
                    "display": "slider" 
                }),
                "brightness": ("FLOAT", {
                    "default": 0, 
                    "min": -100, 
                    "max": 100, 
                    "step": 5,
                    "precision": 200,
                    "display": "slider" 
                }),
                "contrast": ("FLOAT", {
                    "default": 0, 
                    "min": -100, 
                    "max": 100, 
                    "step": 5,
                    "precision": 200,
                    "display": "slider" 
                }),
                "saturation": ("FLOAT", {
                    "default": 0, 
                    "min": -100, 
                    "max": 100, 
                    "step": 5,
                    "precision": 200,
                    "display": "slider" 
                }),
                "gamma": ("INT", {
                    "default": 1, 
                    "min": -0.2, 
                    "max": 2.2, 
                    "step": 0.1,
                    "precision": 200,
                    "display": "slider" 
                }),
                "blur": ("INT", {
                    "default": 0, 
                    "min": -200, 
                    "max": 200, 
                    "step": 1,
                    "precision": 200,
                    "display": "slider" 
                }),
            },
        }
    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "color_correct"
    CATEGORY = "2🐕/🖼️Image/🪞Filter"
    def color_correct(
        self,
        image: torch.Tensor,
        temperature: float,
        hue: float,
        brightness: float,
        contrast: float,
        saturation: float,
        gamma: float,
        blur: float,
    ):
        batch_size, height, width, _ = image.shape
        result = torch.zeros_like(image)
        brightness /= 100
        contrast /= 100
        saturation /= 100
        temperature /= 100
        brightness = 1 + brightness
        contrast = 1 + contrast
        saturation = 1 + saturation
        for b in range(batch_size):
            tensor_image = image[b].numpy()
            modified_image = Image.fromarray((tensor_image * 255).astype(np.uint8))
            # brightness
            modified_image = ImageEnhance.Brightness(modified_image).enhance(brightness)
            # contrast
            modified_image = ImageEnhance.Contrast(modified_image).enhance(contrast)
            modified_image = np.array(modified_image).astype(np.float32)
            # temperature
            if temperature > 0:
                modified_image[:, :, 0] *= 1 + temperature
                modified_image[:, :, 1] *= 1 + temperature * 0.4
            elif temperature < 0:
                modified_image[:, :, 2] *= 1 - temperature
            modified_image = np.clip(modified_image, 0, 255) / 255
            # gamma
            modified_image = np.clip(np.power(modified_image, gamma), 0, 1)
            # saturation
            hls_img = cv2.cvtColor(modified_image, cv2.COLOR_RGB2HLS)
            hls_img[:, :, 2] = np.clip(saturation * hls_img[:, :, 2], 0, 1)
            modified_image = cv2.cvtColor(hls_img, cv2.COLOR_HLS2RGB) * 255
            # hue
            hsv_img = cv2.cvtColor(modified_image, cv2.COLOR_RGB2HSV)
            hsv_img[:, :, 0] = (hsv_img[:, :, 0] + hue) % 360
            modified_image = cv2.cvtColor(hsv_img, cv2.COLOR_HSV2RGB)
            # blur
            if blur > 0:
                modified_image = cv2.GaussianBlur(modified_image, (blur*2+1, blur*2+1), 0)
            modified_image = modified_image.astype(np.uint8)
            modified_image = modified_image / 255
            modified_image = torch.from_numpy(modified_image).unsqueeze(0)
            result[b] = modified_image
        return (result,)

