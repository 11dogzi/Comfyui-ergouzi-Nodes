import torch
import torch.nn.functional as F

class EGZZBYYHNode:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "mask": ("MASK", {}),
            },
            "optional": {
                "Fuzzy_weight": ("INT", {"default": 50, "min": 1, "max": 1000, "step": 2}),
                "Blur_size": ("INT", {"default": 50, "min": 1, "max": 1000, "step": 1}),
            },
        }

    RETURN_TYPES = ("MASK",)
    RETURN_NAMES = ("mask",)
    FUNCTION = "gaussian_blur_edge"
    CATEGORY = "2🐕/⛱️Mask/🪶Fuzzy feathering"

    def gaussian_blur_edge(self, mask, Fuzzy_weight=5, Blur_size=1):
        binary_mask = (mask > 0.5).float()
        
        sigma_float = Blur_size / 10.0
        
        kernel_size_half = Fuzzy_weight // 2
        x = torch.linspace(-kernel_size_half, kernel_size_half, Fuzzy_weight)
        x_grid = x.repeat(Fuzzy_weight).view(Fuzzy_weight, Fuzzy_weight)
        y_grid = x_grid.t()
        gaussian_kernel = torch.exp(-(x_grid**2 + y_grid**2) / (2 * sigma_float**2))
        gaussian_kernel /= gaussian_kernel.sum()
        kernel = gaussian_kernel.view(1, 1, Fuzzy_weight, Fuzzy_weight).repeat(1, 1, 1, 1).to(mask.device)
        blurred_mask = F.conv2d(binary_mask.unsqueeze(0), kernel, padding=kernel_size_half, groups=1).squeeze(0)
        return (blurred_mask,)


