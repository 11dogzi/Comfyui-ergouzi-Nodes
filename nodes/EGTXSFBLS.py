import torch
def common_upscale(samples, width, height, upscale_method, crop):
        if crop == "center":
            old_width = samples.shape[3]
            old_height = samples.shape[2]
            old_aspect = old_width / old_height
            new_aspect = width / height
            x = 0
            y = 0
            if old_aspect > new_aspect:
                x = round((old_width - old_width * (new_aspect / old_aspect)) / 2)
            elif old_aspect < new_aspect:
                y = round((old_height - old_height * (old_aspect / new_aspect)) / 2)
            s = samples[:,:,y:old_height-y,x:old_width-x]
        else:
            s = samples

        if upscale_method == "bislerp":
            return bislerp(s, width, height)
        elif upscale_method == "lanczos":
            return lanczos(s, width, height)
        else:
            return torch.nn.functional.interpolate(s, size=(height, width), mode=upscale_method)

class EGTXSFBLSNode:
    upscale_methods = ["nearest-exact", "bilinear", "area", "bicubic", "lanczos"]
    crop_methods = ["disabled", "center"]
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {"image": ("IMAGE",),
                             "width": ("INT", {"default": 512, "min": 0, "max": 10000, "step": 1}),
                             "height": ("INT", {"default": 512, "min": 0, "max": 10000, "step": 1}),
                             "crop": (s.crop_methods,)},
                "optional": {"upscale_method": (s.upscale_methods,),
                             "lock_aspect_ratio": ("BOOLEAN", {"default": False}),
                             }
                }
    RETURN_TYPES = ("IMAGE", "INT", "INT")
    RETURN_NAMES =('image', 'width', 'height')
    FUNCTION = "upscale"
    CATEGORY = "2🐕/🖼️Image"
    def upscale(self, image, upscale_method, width, height, crop, lock_aspect_ratio=False):
        if width == 0 and height == 0:
            s = image
            return_width = image.shape[3]
            return_height = image.shape[2]
        else:
            samples = image.movedim(-1,1)
            original_width, original_height = samples.shape[3], samples.shape[2]
            original_aspect = original_width / original_height
            if not lock_aspect_ratio:
                if width == 0:
                    width = original_width
                if height == 0:
                    height = original_height
            else:
                if width != 0 and height != 0:
                    if width > height:
                        height = max(1, round(width / original_aspect))
                    else:
                        width = max(1, round(height * original_aspect))
                elif width != 0 and height == 0:
                    height = max(1, round(width / original_aspect))
                elif width == 0 and height != 0:
                    width = max(1, round(height * original_aspect))
            s = common_upscale(samples, width, height, upscale_method, crop)
            s = s.movedim(1,-1)
            return_width = width
            return_height = height
        return (s, return_width, return_height)
