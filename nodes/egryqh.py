NAMESPACE='2🐕Unrestricted switching'

def is_context_empty(ctx):
  return not ctx or all(v is None for v in ctx.values())

def get_category(sub_dirs = None):
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


class EGRYQHNode:

  NAME = get_name("Any Switch")
  CATEGORY = get_category()

  @classmethod
  def INPUT_TYPES(cls):  
    return {
      "required": {},
      "optional": {
        "input01": (any_type,),
        "input02": (any_type,),
        "input03": (any_type,),
        "input04": (any_type,),
        "input05": (any_type,),
        "input06": (any_type,),
      },
    }

  RETURN_TYPES = (any_type,)
  RETURN_NAMES = ('output',)
  FUNCTION = "switch"
  CATEGORY = "2🐕/🆎Choice"

  def switch(self, input01=None, input02=None, input03=None, input04=None, input05=None,input06=None):
    any_value = None
    if not is_none(input01):
      any_value = input01
    elif not is_none(input02):
      any_value = input02
    elif not is_none(input03):
      any_value = input03
    elif not is_none(input04):
      any_value = input04
    elif not is_none(input05):
      any_value = input05
    elif not is_none(input06):
      any_value = input06
    return (any_value,)

NODE_CLASS_MAPPINGS = { "EG_WXZ_QH" : EGRYQHNode }
NODE_DISPLAY_NAME_MAPPINGS = { "EG_WXZ_QH" : "2🐕Unrestricted switching" }

