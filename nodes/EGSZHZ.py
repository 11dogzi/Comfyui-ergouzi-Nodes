NAMESPACE='2🐕Int Float Text Swap'
def is_context_empty(ctx):
    return not ctx or all(v is None for v in ctx.values())
def get_category(sub_dirs=None):
    if sub_dirs is None:
        return NAMESPACE
    else:
        return "{}/utils".format(NAMESPACE)
def get_name(name):
    return '{} ({})'.format(name, NAMESPACE)
class AnyType(str):
    def __ne__(self, __value: object) -> bool:
        return False
any_type = AnyType("*")
def is_none(value):
    if value is not None:
        if isinstance(value, dict) and 'model' in value and 'clip' in value:
            return is_context_empty(value)
    return value is None
def convert_to_int(value):
    try:
        return int(value)
    except ValueError:
        return None
def convert_to_float(value):
    try:
        return float(value)
    except ValueError:
        return None
def convert_to_str(value):
    return str(value)
class EG_SS_RYZH:
    NAME = get_name("Any Switch")
    CATEGORY = get_category()
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {"Any_input": (any_type,)},
            "optional": {},
        }
    RETURN_TYPES = (any_type, any_type, any_type)
    RETURN_NAMES = ('Int', 'Float', 'Text')
    FUNCTION = "switch"
    CATEGORY = "2🐕/🔢number"
    def switch(self, Any_input=None):
        if Any_input is None:
            return (None, None, None)
        
        int_output = convert_to_int(Any_input)
        float_output = convert_to_float(Any_input)
        str_output = convert_to_str(Any_input)
        
        return (int_output, float_output, str_output)

NODE_CLASS_MAPPINGS = { "EG_SS_RYZH" : EG_SS_RYZH }
NODE_DISPLAY_NAME_MAPPINGS = { "EG_SS_RYZH" : "2🐕Int Float Text Swap" }

