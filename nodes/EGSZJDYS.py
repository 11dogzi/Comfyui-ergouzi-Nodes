import torch
class EGSZJDYS:
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
                "operation": (["+", "-", "x", "÷"], {}),
                "number2": ("STRING", {
                    "multiline": True,
                    "default": ""
                }),
            }
        }
    RETURN_TYPES = ("INT", "FLOAT", "STRING")
    RETURN_NAMES = ("result_int", "result_float", "result_str")
    FUNCTION = "compute"
    CATEGORY = "2🐕/🔢number"
    
    def compute(self, number1, number2, operation):
        try:
            number1 = float(number1)
            number2 = float(number2)
        except ValueError:
            return (None, None, "Invalid input. Please enter a number.")
        
        if operation == "+":
            result = number1 + number2
        elif operation == "-":
            result = number1 - number2
        elif operation == "x":
            result = number1 * number2
        elif operation == "÷":
            if number2 == 0:
                return (None, None, "Cannot divide by zero.")
            result = number1 / number2
        else:
            return (None, None, "Invalid operation.")
        
        if result.is_integer():
            result_str = str(int(result))
        else:
            result_str = str(result)
        
        return (int(result), float(result), result_str)