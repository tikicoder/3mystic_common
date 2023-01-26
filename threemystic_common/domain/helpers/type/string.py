from threemystic_common.base_class.base_common import base


class helper_type_string(base): 
  """This is a set of library wrappers to help around expending string libary"""

  def __init__(self, *args, **kwargs) -> None:
    super().__init__(logger_name= f"helper_type_string", *args, **kwargs)
  
  # isNullOrWhiteSpace
  def is_null_or_whitespace(self, strValue, *args, **kwargs):
    if not strValue:
      return True
    
    if not str(strValue).strip():
      return True
    
    return False
  
  # split_string
  def split(self, string_value, trim_data = True, remove_empty = True, separator = "[,;]", regex_split = True, *args, **kwargs):
    if regex_split:
      return self._main_reference.helper_type().regex().split(
        string_value= string_value,
        trim_data= trim_data,
        remove_empty= remove_empty,
        separator= separator
      )
    
    split_data = string_value.split(separator)
    
    if not remove_empty:
      return split_data if not trim_data else [str(item).strip() if item is not None else item for item in split_data ]
      
    if not trim_data:
      return [item for item in split_data if not self.is_null_or_whitespace(item)]

    return [item.strip() for item in split_data if not self.is_null_or_whitespace(item)]