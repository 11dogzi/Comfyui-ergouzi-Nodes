import json
import os
import random

class EGSJNode:
    JSON_FILE_PATH = 'options.json'
    @classmethod
    def load_category_keys(cls):
        
        current_dir = os.path.dirname(os.path.abspath(__file__))
        
        parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
        
        json_dir = os.path.join(parent_dir, 'json')
        
        json_file_path = os.path.join(json_dir, cls.JSON_FILE_PATH)
        
        
        with open(json_file_path, 'r', encoding='utf-8') as f:
            options = json.load(f)
            cls.CATEGORY_KEYS = list(options.keys())  

    @classmethod
    def INPUT_TYPES(cls):
        if not hasattr(cls, 'CATEGORY_KEYS'):
            cls.load_category_keys()
        
        input_types = {
            "optional": {
                
                "Custom_Type1": (["None"] + cls.CATEGORY_KEYS, {"default": "None"}),
                "weight1": ("FLOAT", {"default": 1.0, "min": 0.1, "max": 2, "step": 0.1, "display": "slider"}),
                "Custom_Type2": (["None"] + cls.CATEGORY_KEYS, {"default": "None"}),
                "weight2": ("FLOAT", {"default": 1.0, "min": 0.1, "max": 2, "step": 0.1, "display": "slider"}),
                "Custom_Type3": (["None"] + cls.CATEGORY_KEYS, {"default": "None"}),
                "weight3": ("FLOAT", {"default": 1.0, "min": 0.1, "max": 2, "step": 0.1, "display": "slider"}),
                "Custom_Type4": (["None"] + cls.CATEGORY_KEYS, {"default": "None"}),
                "weight4": ("FLOAT", {"default": 1.0, "min": 0.1, "max": 2, "step": 0.1, "display": "slider"}),
                "Custom_Type5": (["None"] + cls.CATEGORY_KEYS, {"default": "None"}),
                "weight5": ("FLOAT", {"default": 1.0, "min": 0.1, "max": 2, "step": 0.1, "display": "slider"}),
                "seed": ("INT", {"default": 0, "min": -1125899906842624, "max": 1125899906842624}),
            },
            "required": {
            }
        }
        return input_types

    @staticmethod
    def get_options_keys(key):
        
        current_dir = os.path.dirname(os.path.abspath(__file__))
        
        parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
        
        json_dir = os.path.join(parent_dir, 'json')
        
        json_file_path = os.path.join(json_dir, EGSJNode.JSON_FILE_PATH)
        
        
        with open(json_file_path, 'r', encoding='utf-8') as f:
            options = json.load(f)
            return list(options[key].keys())

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("prompt",)
    FUNCTION = "generate_prompt"
    CATEGORY = "2🐕/🏷️Prompt word master/🔀random class"

    def __init__(self):
        self.load_json()

    def load_json(self):
        
        current_dir = os.path.dirname(os.path.abspath(__file__))
        
        parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
        
        json_dir = os.path.join(parent_dir, 'json')
        
        json_file_path = os.path.join(json_dir, self.JSON_FILE_PATH)
    
        
        with open(json_file_path, 'r', encoding='utf-8') as f:
            self.options = json.load(f)

    def generate_prompt(self, **kwargs):
        prompt_parts = []
        for i in range(1, 6):  
            selected_key = kwargs.get(f"Custom_Type{i}")
            weight = kwargs.get(f"weight{i}", 1.0)
            if selected_key not in self.CATEGORY_KEYS:
                continue
            
            options_keys = [k for k in self.get_options_keys(selected_key) if k != "None"]
            if options_keys:  
                random_choice = random.choice(options_keys)
                
                if random_choice != "None":
                    
                    if weight != 1:
                        prompt_parts.append(f"({self.options[selected_key][random_choice]}:{weight:.1f})")
                    else:
                        prompt_parts.append(self.options[selected_key][random_choice])
        prompt = ','.join(prompt_parts).strip()
        prompt += ','
        return (prompt,) if prompt else ('',)






