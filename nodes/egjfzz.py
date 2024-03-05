import numpy as np
import scipy.ndimage
import torch

def grow(mask, expand, tapered_corners):
    c = 0 if tapered_corners else 1
    kernel = np.array([[c, 1, c],
                            [1, 1, 1],
                            [c, 1, c]])
    mask = mask.reshape((-1, mask.shape[-2], mask.shape[-1]))
    out = []
    for m in mask:
        output = m.numpy()
        for _ in range(abs(expand)):
            if expand < 0:
                output = scipy.ndimage.grey_erosion(output, footprint=kernel)
            else:
                output = scipy.ndimage.grey_dilation(output, footprint=kernel)
        output = torch.from_numpy(output)
        out.append(output)
    return torch.stack(out, dim=0)

def combine(destination, source, x, y):
    output = destination.reshape((-1, destination.shape[-2], destination.shape[-1])).clone()
    source = source.reshape((-1, source.shape[-2], source.shape[-1]))

    left, top = (x, y,)
    right, bottom = (min(left + source.shape[-1], destination.shape[-1]), min(top + source.shape[-2], destination.shape[-2]))
    visible_width, visible_height = (right - left, bottom - top,)

    source_portion = source[:, :visible_height, :visible_width]
    destination_portion = destination[:, top:bottom, left:right]

    
    output[:, top:bottom, left:right] = destination_portion - source_portion

    output = torch.clamp(output, 0.0, 1.0)

    return output

class EGJFZZSC:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            
            "required": {
                "mask": ("MASK",),
                "senerate_width": ("INT", {
                    "default": 10,
                    "min": 1,
                    "max": 666,
                    "step": 1
                }),
                "smooth": ("BOOLEAN", {"default": True}),
            },
            
            "optional": {}
        }

    RETURN_TYPES = ("MASK",)
    RETURN_NAMES = ("mask",)
    FUNCTION = "run"
    CATEGORY = "2🐕/⛱️Mask"

    def run(self, mask, senerate_width, smooth):
        m1 = grow(mask, senerate_width, smooth)
        m2 = grow(mask, -senerate_width, smooth)
        m3 = combine(m1, m2, 0, 0)

        return (m3,)
