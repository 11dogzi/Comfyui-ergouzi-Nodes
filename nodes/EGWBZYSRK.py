import torch
class EGZYWBKNode:
    def __init__(self):
        pass
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "number1": ("STRING", {
                    "multiline": True,
                    "default": ""
                }),
            }
        }
    RETURN_TYPES = ("INT", "FLOAT", "STRING")
    RETURN_NAMES = ("result_int", "result_float", "result_str")
    FUNCTION = "convert_number_types"
    CATEGORY = "2🐕/🗒️Text"
    def convert_number_types(self, number1):
        try:
            float_num = float(number1)
            int_num = int(float_num)
            str_num = number1
        except ValueError:
            return (None, None, number1)
        return (int_num, float_num, str_num)
NODE_CLASS_MAPPINGS = { "EG_ZY_WBK" : EGZYWBKNode }
NODE_DISPLAY_NAME_MAPPINGS = { "EG_ZY_WBK" : "2🐕Free input box" }