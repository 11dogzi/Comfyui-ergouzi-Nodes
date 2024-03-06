class EGRYHT:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {
                    "weight": ("FLOAT", {
                        "default": 1,
                        "min": 0,
                        "max": 1,
                        "step": 0.01,
                        "display": "slider"
                    }),
                },
                "optional": {}
        }
    RETURN_TYPES = ("FLOAT",)
    FUNCTION = "run"
    CATEGORY = "2🐕/🔢number"
    INPUT_IS_LIST = False
    OUTPUT_IS_LIST = (False,)
    def run(self, weight):
        scaled_number = weight
        return (scaled_number,)

