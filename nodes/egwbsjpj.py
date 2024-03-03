import os
import requests
import hashlib
import json
import re
import random
class EGWBSJPJ:
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {},
            "optional": {
                "text1": ("STRING", {"multiline": True}),
                "text2": ("STRING", {"multiline": True}),
                "text3": ("STRING", {"multiline": True}),
                "text4": ("STRING", {"multiline": True}),
                "text5": ("STRING", {"multiline": True}),
                "Splicing_Characters": ("STRING", {"default": ""}),
                "Exclude_Characters": ("STRING", {"default": ""}),
                "Exclude_words": ("STRING", {"default": ""}),
                "seed": ("INT", {"default": 0, "min": -1125899906842624, "max": 1125899906842624})
            },
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ('concatenated_text',)
    FUNCTION = "concatenate_text"
    CATEGORY = "2🐕/🗒️Text"
    
    def concatenate_text(self, text1, text2, text3, text4, text5, Splicing_Characters="", Exclude_Characters="", Exclude_words="", seed=0):
        texts = [text1, text2, text3, text4, text5]
        
        random.seed(seed)
        
        random.shuffle(texts)
        
        concatenated_text = Splicing_Characters.join(filter(None, texts))
        
        if Exclude_Characters:
            exclude_chars = Exclude_Characters.split(',')
            exclude_chars = [char.strip() for char in exclude_chars if char.strip()]
            for char in exclude_chars:
                concatenated_text = concatenated_text.replace(char, "")
        
        if Exclude_words:
            exclude_words = Exclude_words.split(',')
            exclude_words = [word.strip() for word in exclude_words if word.strip()]
            for word in exclude_words:
                pattern = r'(?<!\w)' + re.escape(word) + r'(?!\w)'
                concatenated_text = re.sub(pattern, '', concatenated_text)
        
        concatenated_text = re.sub(r'(\W)\1+', r'\1', concatenated_text)
        concatenated_text = re.sub(r'^[，,]+', '', concatenated_text)
        concatenated_text = re.sub(r'[，,]+$', '', concatenated_text)
        
        return (concatenated_text,)
NODE_CLASS_MAPPINGS = { "EG_SJPJ_Node" : EGWBSJPJ }
NODE_DISPLAY_NAME_MAPPINGS = { "EG_SJPJ_Node" : "2🐕Text random splicing" }
