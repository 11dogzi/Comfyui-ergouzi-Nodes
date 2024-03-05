import json
import os

class EGTSCMBGLNode:
    JSON_FILE_PATH = '../json/egtscglds.json'  
    @classmethod
    def load_options(cls):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        json_file_path = os.path.join(current_dir, cls.JSON_FILE_PATH)
        directory = os.path.dirname(json_file_path)
        
        
        if not os.path.exists(directory):
            os.makedirs(directory)
        
        
        if os.path.exists(json_file_path):
            with open(json_file_path, 'r', encoding='utf-8') as f:
                try:
                    cls.options = json.load(f)
                except json.JSONDecodeError:
                    print("Template file format error, a new template file will be created for you。")
                    cls.options = {}
        else:
            print("The template file does not exist. We will create a new template file for you。")
            cls.options = {}
            cls.save_options()
    @classmethod
    def save_options(cls):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        json_file_path = os.path.join(current_dir, cls.JSON_FILE_PATH)
        directory = os.path.dirname(json_file_path)
        
        
        if not os.path.exists(directory):
            os.makedirs(directory)
        
        
        with open(json_file_path, 'w', encoding='utf-8') as f:
            json.dump(cls.options, f, ensure_ascii=False, indent=4)

    @classmethod
    def INPUT_TYPES(cls):
        cls.load_options()  
        keys_list = list(cls.options.keys())  
        default_key = keys_list[0] if keys_list else 'None'  
        return {
            "optional": {
                "Read": (keys_list, {"default": default_key}),
                "New_Name": ("STRING", {"default": "Please enter a name"}),
                "New_Content": ("STRING", {"default": "Please enter the content"}),
                "Function": (["Read", "New", "Delete"], {"default": "Read"}),
            },
            "required": {
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("Text",)
    FUNCTION = "process_action"
    CATEGORY = "2🐕/🏷️Prompt word master/✍️custom"

    def process_action(self, Read='None', New_Name='Please enter a name', New_Content='Please enter the content', Function='Read'):
        self.load_options()
        if Function == 'New':
            print("2🐕Successfully saved for you, more SD tutorials are available at B站@灵仙儿和二狗子")
            self.options[New_Name] = New_Content
            self.save_options()
            
            self.load_options()
            return ("2🐕Successfully saved for you, more SD tutorials are available at B站@灵仙儿和二狗子",)
        elif Function == 'Delete':
            if Read in self.options:
                print("2🐕Successfully deleted for you, more SD tutorials are available at B站@灵仙儿和二狗子")
                del self.options[Read]
                self.save_options()
                
                self.load_options()
                return ("2🐕Successfully deleted for you, more SD tutorials are available at B站@灵仙儿和二狗子",)
            else:
                return ("2🐕We have checked that the template does not exist for you. More SD tutorials are available at B站@灵仙儿和二狗子",)
                print("2🐕We have checked that the template does not exist for you. More SD tutorials are available at B站@灵仙儿和二狗子")
        elif Function == 'Read':
            if not Read or Read not in self.options:
                print("2🐕We have checked that the template does not exist for you. More SD tutorials are available at B站@灵仙儿和二狗子")
                return ("2🐕We have checked that the template does not exist for you. More SD tutorials are available at B站@灵仙儿和二狗子",)
            else:
                
                print(f"2🐕We have successfully read it for you. The template content is as follows. More SD tutorials are available at B站@灵仙儿和二狗子：")
                print(self.options[Read])
                
                return (self.options[Read],)
        else:
            return ("2🐕Operation error, please refresh the page. More SD tutorials are available at B站@灵仙儿和二狗子",)
            print("2🐕Operation error, please refresh the page. More SD tutorials are available at @灵仙儿和二狗子")





