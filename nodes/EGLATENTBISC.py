import torch
class Args:
    def __init__(self):
        self.gpu_only = False
args = Args()
def intermediate_device():
    if args.gpu_only:
        return get_torch_device()
    else:
        return torch.device("cpu")
class EGKLATENT:
    ratios = {
        "1:1": (1, 1),
        "3:2": (3, 2),
        "16:9": (16, 9),
        "2:3": (2, 3),
        "9:16": (9, 16)
    }

    def __init__(self):
        self.device = intermediate_device()

    @classmethod
    def INPUT_TYPES(s):
        return {"required": {"width": ("INT", {"default": 512, "min": 16, "max": 4096, "step": 8}),
                             "height": ("INT", {"default": 512, "min": 16, "max": 4096, "step": 8}),
                             "ratio": (list(s.ratios.keys()), {"default": "1:1"}),
                             "batch_size": ("INT", {"default": 1, "min": 1, "max": 4096}),
                             "equal_scale": ("BOOLEAN", {"default": False})
                             }}

    RETURN_TYPES = ("LATENT", "INT", "INT")
    RETURN_NAMES = ('LATENT', 'width', 'height')
    FUNCTION = "generate"
    CATEGORY = "2🐕/🤿Latent"

    def generate(self, width, height, batch_size=1, ratio="1:1", equal_scale=False):
        if ratio not in self.ratios.keys():
            raise ValueError(f"Invalid ratio value: {ratio}. Valid ratios are: {', '.join(self.ratios.keys())}")
        if not equal_scale:
            latent = torch.zeros([batch_size, 4, int(height // 8), int(width // 8)], device=self.device)
            return ({"samples": latent}, width, height)
        if width == height:
            max_dim = width
            ratio_width, ratio_height = self.ratios[ratio]
            if ratio_width >= ratio_height:
                width = max_dim
                height = int(max_dim * ratio_height / ratio_width)
            else:
                height = max_dim
                width = int(max_dim * ratio_width / ratio_height)
        else:
            max_dim = max(width, height)
            ratio_width, ratio_height = self.ratios[ratio]
            if width == max_dim:
                new_height = int(max_dim * ratio_height / ratio_width)
                height = new_height
            elif height == max_dim:
                new_width = int(max_dim * ratio_width / ratio_height)
                width = new_width

        latent = torch.zeros([batch_size, 4, int(height // 8), int(width // 8)], device=self.device)
        return ({"samples": latent}, width, height)
