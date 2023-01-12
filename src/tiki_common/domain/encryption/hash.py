from base_class.base_common import base

class encryption_hash(base): 
  """This is a set of library wrappers to help monitor performance"""

  def __init__(self, *args, **kwargs) -> None:
    super().__init__(*args, **kwargs)
    self._hash_method = self.__get_hash_method(*args, **kwargs)
  
  def __get_hash_method(self, hash_method, *args, **kwargs):
    if self._main_reference.helper_type().general().is_null_or_whitespace(hash_method):
      raise self._main_reference.exception().exception(
        exception_type = "argument"
      ).not_implemented(
        name = "hash_method",
        message = f"argument not provided"
      )

    if hash_method.lower() == "sha1":
      from hashlib import sha1
      return sha1
    
    raise self._main_reference.exception().exception(
        exception_type = "generic"
      ).not_implemented(
        name = "hash_method",
        message = f"Unknown Hash Method Provided: {hash_method}"
      )
    

  def generate_hash_fromobject(self, data, *args, **kwargs):
    if self._main_reference.helper_type().general().is_type(data, str):
      return self._hash_method(data.encode("utf-8")).hexdigest()
    
    return self._hash_method(self._main_reference.helper_json().dumps(data= data).encode("utf-8")).hexdigest()