NAMESPACE='2🐕Choice Switch'

def is_context_empty(ctx):
  """Checks if the provided ctx is None or contains just None values."""
  return not ctx or all(v is None for v in ctx.values())

def get_category(sub_dirs = None):
    if sub_dirs is None:
        return NAMESPACE
    else:
        return "{}/utils".format(NAMESPACE)

def get_name(name):
    return '{} ({})'.format(name, NAMESPACE)

class AnyType(str):
  """A special class that is always equal in not equal comparisons. Credit to pythongosssss"""

  def __ne__(self, __value: object) -> bool:
    return False


any_type = AnyType("*")


def is_none(value):
  """Checks if a value is none. Pulled out in case we want to expand what 'None' means."""
  if value is not None:
    if isinstance(value, dict) and 'model' in value and 'clip' in value:
      return is_context_empty(value)
  return value is None


class EGXZQHNode:
  """The any switch. """

  NAME = get_name("Select output")
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
        "choice": (["1", "2", "3", "4", "5", "6"],)
      },
    }

  RETURN_TYPES = (any_type,)
  RETURN_NAMES = ('output',)
  FUNCTION = "switch"
  CATEGORY = "2🐕/🆎Choice"

  def switch(self, input01=None, input02=None, input03=None, input04=None, input05=None, input06=None, choice=None):
    """Chooses the item to output based on the user's selection."""
    if choice is not None:
        if choice == "1":
            return (input01,)
        elif choice == "2":
            return (input02,)
        elif choice == "3":
            return (input03,)
        elif choice == "4":
            return (input04,)
        elif choice == "5":
            return (input05,)
        elif choice == "6":
            return (input06,)
        else:
            return (None,)

