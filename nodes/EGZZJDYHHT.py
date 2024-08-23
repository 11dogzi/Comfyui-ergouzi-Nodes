from PIL import Image, ImageFilter
import torch
import numpy as np

def tensortopil(image):
    return Image.fromarray(np.clip(255. * image.cpu().numpy().squeeze(), 0, 255).astype(np.uint8))
def piltotensor(image):
    return torch.from_numpy(np.array(image).astype(np.float32) / 255.0).unsqueeze(0)

class EGZZMHHT:
    @classmethod
    def INPUT_TYPES(s):
        return {
                "required": {
                                "mask": ("MASK",),
                                "Fuzzyintensity":("INT", {"default": 1, 
                                                        "min":0, 
                                                        "max": 150, 
                                                        "step": 1,
                                                        "display": "slider"})
                            }
            }
    
    RETURN_TYPES = ('MASK',)
    FUNCTION = "maskmohu"
    CATEGORY = "2🐕/Mask/Fuzzy fast intensity"
    INPUT_IS_LIST = False
    OUTPUT_IS_LIST = (False,)
    def maskmohu(self,mask,Fuzzyintensity):
        print('SmoothMask',mask.shape)
        mask=tensortopil(mask)
        feathered_image = mask.filter(ImageFilter.GaussianBlur(Fuzzyintensity))

        mask=piltotensor(feathered_image)
           
        return (mask,)
